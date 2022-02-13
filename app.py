from flask import Flask, render_template, request, flash, g, session
import sqlite3, random

# Create instance of Flask by calling its class constructor
app = Flask(__name__)
app.secret_key = "12ev@09_9kT;bjs8$32jhbd_sjhAdhc%mhn_773gvsahG/HSI*IH_jbs"

# cookie name for sessions
app.config['SESSION_COOKIE_NAME'] = "75jhbkdaCooKiebMONsteRRs!7)^&hbsh$4)"

# sessions in flask allows us to share data
# between different functions 
# w/ sessions, we're working in global scope

@app.route('/', methods=['POST', 'GET'])
def index():
    session["all_courses"], session["checklist_courses"] = get_db()
    return render_template('index.html', all_courses=session["all_courses"], 
                            checklist_names=session["checklist_courses"])


@app.route('/add_class', methods=['POST'])
def add_class():
    session["checklist_courses"].append(request.form["select_courses"])
    return render_template('index.html', all_courses=session["all_courses"], 
                            checklist_names=session["checklist_courses"])


@app.route('/remove_class', methods=['POST'])
def remove_class():
    checkboxes = request.form.getlist("check")

    for choice in checkboxes:
        if choice in session["checklist_courses"]:
            pos = session['checklist_courses'].index(choice)
            session["checklist_courses"].pop(pos)
            session.modified = True

    return render_template('index.html', all_courses=session["all_courses"], 
                            checklist_names=session["checklist_courses"])


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('course_list.db')
        cursor = db.cursor()
        cursor.execute("select * from courses")
        all_data = cursor.fetchall()
        # list comprehension to get only string w/o tuples
        all_names = [str(tup[1]) for tup in all_data]

        checklist = all_names.copy()
        random.shuffle(checklist)
        checklist = checklist[::4] # get up to 3 items as random
    # return a tuple
    return all_names, checklist


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# run app
if __name__ == '__main__':
	app.run(debug=True)