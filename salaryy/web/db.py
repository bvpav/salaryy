import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """Get the current database connection, or create one, if none exists."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES,
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """Close the current database connection, if one exists. Called after every request."""
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """Initialize the database and execute the schema."""

    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

