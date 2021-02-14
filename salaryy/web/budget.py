from flask import Blueprint, render_template

from .auth import login_required

bp = Blueprint('budget', __name__)


@bp.route('/')
@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('budget/dashboard.html')

