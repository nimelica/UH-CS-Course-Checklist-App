import sqlite3, requests

# Get data from the Mock API using GET HTTP method
# response data type will be byte
response = requests.get("https://uh-cs-requirements.herokuapp.com/courses")

# Check if the request was successful
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')


# Convert bytes into a JSON list data
courses = response.json()

# Create an empty database
connection = sqlite3.connect('course_list.db')

# communication with database via cursor with SQL commands
cursor = connection.cursor()

# Create table
cursor.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")

# Fill that table
for i in range(len(courses)):
    cursor.execute("INSERT INTO courses (name) values (?)", [courses[i]])


# Do not forget to save (commit) and close the database connection
connection.commit()
connection.close()