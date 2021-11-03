from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import sqlite3 as sql

conn = sql.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE Accounts(firstName TEXT, lastName TEXT, email EMAIL, username TEXT, password TEXT)')
print ("Table created successfully")
conn.close()

app = Flask(__name__)
CORS(app)

@app.route('/register')
def register():
    return 'Hello, World!'

@app.route('/register', methods=['POST'])
def create_task():
    print(request)
    if not request.json:
        abort(400)

    print(request.json)

    # print(request.json)
    # task = {
    #     'id': tasks[-1]['id'] + 1,
    #     'title': request.json['title'],
    #     'description': request.json.get('description', ""),
    #     'done': False
    # }
    # tasks.append(task)
    return jsonify({'task': "Nothing"}), 201

def create_account():
    if request.method == 'POST':
        try:
            firstName = request.form['firstname']
            lastName = request.form['lastname']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Accounts(firstName,lastName,email,username,password) VALUES (?,?,?,?,?)",(firstName,lastName,email,username,password))

            con.commit()
            msg = "Record successfully added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            # return render_template("result.html",msg = msg)
            for row in cur.execute("SELECT * FROM Accounts"):
                print(row)
            con.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)