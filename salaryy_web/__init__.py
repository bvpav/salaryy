import os

from flask import Flask, render_template


def create_app():
    """Create and configure the app."""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'salaryy.sqlite'),
    )

    # Load config from instance directory
    app.config.from_pyfile('config.py', silent=True)

    # Make sure that the instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # A basic landing page
    @app.route('/')
    def hello():
        return render_template('dashboard.html')

    @app.route('/detail/<string:employee_name>')
    def detail(employee_name):
        return render_template('detail.html')

    return app

