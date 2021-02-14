from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint('employee', __name__, url_prefix='/employee')


@bp.route('/detail/<string:employee_name>')
@login_required
def detail(employee_name):
    return render_template('employee/detail.html', employee_name=employee_name)

