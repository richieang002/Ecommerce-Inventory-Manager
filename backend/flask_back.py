from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import sqlite3 as sql

try:
    conn = sql.connect('database.db')
    print ("Opened database successfully")

    conn.execute('CREATE TABLE Accounts(firstName TEXT, lastName TEXT, email EMAIL UNIQUE, username TEXT, password TEXT)')
    print ("Table created successfully")
    conn.close()
except:
    print("Table already initialised, app is working")
    conn.close()

app = Flask(__name__)
CORS(app)

@app.route('/register', methods=['POST'])
def create_account():
    if request.method == 'POST':
        try:
            firstName = request.json['firstname']
            lastName = request.json['lastname']
            email = request.json['email']
            username = request.json['username']
            password = request.json['password']
            print(firstName)
            
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Accounts(firstName,lastName,email,username,password) VALUES (?,?,?,?,?)",(firstName,lastName,email,username,password))
            
            con.commit()
            msg = "Record successfully added"

        except sql.IntegrityError:
            print("couldn't add email twice")
            
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            # return render_template("result.html",msg = msg)
            for row in cur.execute("SELECT * FROM Accounts"):
                print(row)
            con.close()

    return jsonify({'task': "Successfully"}), 201


@app.route('/login', methods=['POST'])
def login_account():
    if request.method == 'POST':
        try:
            email = request.json['email']
            password = request.json['password']

            with sql.connect("database.db") as con:
                cur = con.cursor()
               
                # cur.execute("SELECT COUNT(*) FROM Accounts WHERE email=?)",(email))
                cur.execute("SELECT email,password FROM Accounts WHERE email=? AND password=?",[email,password])
                credentials = cur.fetchone()

                if credentials is None:
                    print("User not found")
                    return abort(400)
                else:
                    print("Login Successful")
                # for x,y in credentials:
                #     print(x,y)
                #     if email == x and password == y:
                #         print("Login Successful")
                #         break

            con.commit()

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            # return render_template("result.html",msg = msg)
            con.close()

    return jsonify({'task': "Successfully"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)