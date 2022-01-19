from distutils.log import debug
from flask import Flask, render_template, request
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'crud_db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()
mysql.init_app(app)


@app.route("/")
def index():
    cursor = mysql.connection.cursor()
    cursor.execute(f"use newsstand_db;")
    cursor.execute(f"SELECT * FROM `sites`;")
    cursor.execute(f"SELECT news.*, ed.* FROM sites AS news, editors AS ed WHERE news.ed_id = ed.ed_id;")

    np_list = cursor.fetchall()
    cursor.close()

    return render_template("index.html", len = len(np_list), np_list = np_list)

@app.route("/help")
def help():
    return render_template ("help.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



    




