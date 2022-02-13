from flask import Flask, render_template, request, flash, g, session
import sqlite3, random

# Create instance of Flask by calling its class constructor
app = Flask(__name__)
app.secret_key = "12ev@09_9kT;bjs8$32jhbd_sjhAdhc%mhn_773gvsahG/HSI*IH_jbs"


@app.route('/')
def index():
    item = get_db()
    return item[0]


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('course_list.db')
        cursor = db.cursor()
        cursor.execute("select name from courses")
        all_tuples = cursor.fetchall()
        all_names = [str(tup[0]) for tup in all_tuples]

    return all_names


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# run app
if __name__ == '__main__':
	app.run(debug=True)