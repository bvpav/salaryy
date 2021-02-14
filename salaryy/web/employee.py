import functools

from flask import Blueprint, render_template, request, g, flash, redirect, url_for
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

bp = Blueprint('employee', __name__, url_prefix='/employee')


def get_employee(employee_name):
    employee = get_db().execute(
        'SELECT * FROM employee WHERE employer_id = ? AND name=?',
        (g.user['id'], employee_name)
    ).fetchone()

    if employee is None:
        abort(404, f'Employee {employee_name} not found.')

    return employee


@bp.route('/add', methods=('GET', 'POST'))
@login_required
def add():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        employee_salary = request.form['employee_salary']
        db = get_db()
        error = None

        if not employee_name:
            error = 'Name is required'
        elif db.execute(
            'SELECT * from employee WHERE name = ? AND employer_id = ?',
            (employee_name, g.user['id'])
        ).fetchone() is not None:
            error = 'Name must be unique'
        elif employee_salary:
            try:
                employee_salary = float(employee_salary)
            except ValueError:
                error = 'Salary must be a number'
            else:
                if employee_salary < 0.0:
                    error = 'Salary can\'t be negative'

        if error is None:
            db.execute(
                'INSERT INTO employee (employer_id, name, salary) values (?, ?, ?)',
                (g.user['id'], employee_name, employee_salary)
            )
            db.commit()
            flash(f'Employee {employee_name} successfully added')
            return redirect(url_for('budget.dashboard'))

        flash(error)

    return render_template('employee/add.html')


@bp.route('/detail/<string:employee_name>', methods=('GET', 'POST'))
@login_required
def detail(employee_name):
    employee = get_employee(employee_name)
    return render_template('employee/detail.html', employee=employee)

@bp.route('/edit/<string:employee_name>', methods=('GET', 'POST'))
@login_required
def edit(employee_name):
    employee = get_employee(employee_name)

    if request.method == 'POST':
        # XXX: Repeating code fron add()
        employee_name = request.form['employee_name']
        employee_salary = request.form['employee_salary']
        db = get_db()
        error = None

        if not employee_name:
            error = 'Name is required'
        elif db.execute(
            'SELECT * from employee WHERE id != ? AND name = ? AND employer_id = ?',
            (employee['id'], employee_name, g.user['id'])
        ).fetchone() is not None:
            error = 'Name must be unique'
        elif employee_salary:
            try:
                employee_salary = float(employee_salary)
            except ValueError:
                error = 'Salary must be a number'
            else:
                if employee_salary < 0.0:
                    error = 'Salary can\'t be negative'

        if error is None:
            db.execute(
                'UPDATE employee SET name = ?, salary = ? WHERE id = ?',
                (employee_name, employee_salary, employee['id'])
            )
            db.commit()
            flash(f'Employee {employee_name} successfully updated')
            return redirect(url_for('budget.dashboard'))

        flash(error)

    return render_template('employee/add.html', employee=employee)


@bp.route('/delete/<string:employee_name>', methods=('POST',))
def delete(employee_name):
    employee = get_employee(employee_name)
    db = get_db()
    db.execute('DELETE FROM employee WHERE id = ?', (employee['id'],))
    db.commit()
    return redirect(url_for('budget.dashboard'))

