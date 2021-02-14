from flask import Blueprint, render_template, g

from .auth import login_required
from .db import get_db

bp = Blueprint('budget', __name__)


@bp.route('/')
@bp.route('/dashboard')
@login_required
def dashboard():
    db = get_db()
    employees = db.execute(
        'SELECT * FROM employee WHERE employer_id = ?',
        (g.user['id'],)
    ).fetchall()
    return render_template('budget/dashboard.html', employees=employees)

