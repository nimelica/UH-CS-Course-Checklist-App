from flask import Flask, render_template, request, flash, g, session
import sqlite3, random

# Create instance of Flask by calling its class constructor
app = Flask(__name__)
app.secret_key = "12ev@09_9kT;bjs8$32jhbd_sjhAdhc%mhn_773gvsahG/HSI*IH_jbs"


@app.route('/')
def index():
    return "HELLO"


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('course_list.db')
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# run app
if __name__ == '__main__':
	app.run(debug=True)