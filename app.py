from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import db_config

app = Flask(__name__)

app.config['MYSQL_HOST'] = db_config.MYSQL_HOST
app.config['MYSQL_USER'] = db_config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = db_config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = db_config.MYSQL_DB
app.config['MYSQL_PORT'] = db_config.MYSQL_PORT

mysql = MySQL(app)

@app.route('/get-sgusers', methods=['GET'])
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM cam_users")
    users = cur.fetchall()
    return jsonify(users), 200;

# @app.route('/add_user', methods=['POST'])
# def add_user():
#     name = request.form['name']
#     email = request.form['email']
#     cur = mysql.connection.cursor()
#     cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
#     mysql.connection.commit()
#     return jsonify({"status": "User added"}), 200

if __name__ == '__main__':
    app.run(debug=True,  port=5000)
