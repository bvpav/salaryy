from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint('budget', __name__)


@bp.route('/')
@login_required
def dashboard():
    return render_template('budget/dashboard.html')


@bp.route('/detail/<string:employee_name>')
@login_required
def detail(employee_name):
    return render_template('budget/detail.html', employee_name=employee_name)

