from flask import Flask, render_template

app = Flask(__name__)

import mysql.connector

con = mysql.connector.connect(
    host="sql11.freemysqlhosting.net",
    user="sql11481503",
    password="CBDLzgEwRq",
    database="sql11481503",
    auth_plugin="mysql_native_password")

class User:
    def __init__(self, id, user_id, firstname, lastname, distance, type, procent):
        self.id = id
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.distance = distance
        self.type = type
        self.procent = procent

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Tour_de_GlobalLogic')
def tdgl():
    query = "SELECT user.id, activity.user_id, stats.firstname, stats.lastname, SUM(activity.distance) AS distance, activity.type FROM user, activity, stats WHERE activity.user_id = user.id AND user.stats_id = stats.id GROUP BY user_id"
    cur = con.cursor()
    cur.execute(query)

    listaUserow = []
    for (id, user_id, firstname, lastname, distance, type) in cur:
        zm = (distance/1000) * 100
        user = User(id, user_id, firstname, lastname, distance, type, round(zm, 1))
        listaUserow.append(user)
    return render_template("tdgl.html", listaUserow=listaUserow)

@app.route('/Monthly_Cup')
def mc():
    query = "SELECT user.id, activity.user_id, stats.firstname, stats.lastname, SUM(activity.distance) AS distance, activity.type FROM user, activity, stats WHERE activity.user_id = user.id AND user.stats_id = stats.id GROUP BY user_id"
    cur = con.cursor()
    cur.execute(query)

    listaUserow = []
    for (id, user_id, firstname, lastname, distance, type) in cur:
        zm = (distance / 1000) * 100
        user = User(id, user_id, firstname, lastname, distance, type, round(zm, 1))
        listaUserow.append(user)
    return render_template("mc.html", listaUserow=listaUserow)

if __name__ == "__main__":
    app.run(debug=True)
