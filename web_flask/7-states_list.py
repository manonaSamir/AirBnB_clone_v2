#!/usr/bin/python3
"""Starts a Flask web application.
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)



app = Flask(__name__)
app.url_map.strict_slashes = False




@app.route('/states_list')
def states():
    """ Display list of all the states """
    states = storage.all(State)
    states_list = list(states.values())
    return render_template('7-states_list.html', states=states_list)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all("State")
    states_list = list(states.values())
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
