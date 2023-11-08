import json
from flask import Flask
from flask_cors import CORS
# import MySQLdb

app = Flask(__name__)
CORS(app)

# API

@app.route('/')
def test_api():
    return json.dumps({
        'message':'thanks for testing the api',
    })

# @app.route('/db')
# def db_api():
#     connection = MySQLdb.connect(
#         host='mysql',
#         user='project',
#         passwd='project',
#         db='users')
#     cursor = connection.cursor()

    cursor.execute("""SHOW CREATE DATABASE test_database;
    """)

    myresult = cursor.fetchall()

    for row in myresult:
        print(row)

    connection.close()
    return json.dumps({
        'message':'thanks for db testing',
    })


app.run()