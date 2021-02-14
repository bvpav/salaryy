from flask import Blueprint, render_template, request, g, flash, redirect, url_for

from .auth import login_required
from .db import get_db

bp = Blueprint('employee', __name__, url_prefix='/employee')


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
    return render_template('employee/detail.html', employee_name=employee_name)

