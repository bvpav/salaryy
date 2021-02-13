from flask import Blueprint, render_template

bp = Blueprint('budget', __name__)


@bp.route('/')
def dashboard():
    return render_template('dashboard.html')


@bp.route('/detail/<string:employee_name>')
def detail(employee_name):
    return render_template('detail.html', employee_name=employee_name)

