from distutils.log import debug
from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os # needed for future functionality


app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'crud_db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER'
UPLOAD_FOLDER = '/static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

mysql = MySQL()
mysql.init_app(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['POST','GET'])
@app.route("/home", methods=['POST','GET'])
def index():
    cursor = mysql.connection.cursor()
    cursor.execute(f"use newsstand_db;")
    cursor.execute(f"SELECT * FROM `sites`;")
    cursor.execute(f"SELECT news.*, ed.* FROM sites AS news, editors AS ed WHERE ed.news_id = news.news_id;")
    np_list = cursor.fetchall()
    cursor.close()

    return render_template("index.html", len = len(np_list), np_list = np_list)



@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        if request.form['name'] != "" and  request.form['url'] != "": 
            cursor = mysql.connection.cursor()
            cursor.execute(f"use newsstand_db;")
            Name = request.form['name']
            Site = request.form['url']
            ed_firstname = request.form['ed_firstname']
            ed_lastname = request.form['ed_lastname']
            ed_datestarted = request.form['ed_datestarted']
            cursor.execute(f"INSERT INTO `sites`  (`news_name`, `news_url`) VALUES ('{Name}','{Site}');")
            mysql.connection.commit()                 
            cursor.execute(f" SELECT news_id from `sites` WHERE  news_name = '{Name}'")
            News_id = cursor.fetchone ()
            News_int = News_id["news_id"]
            cursor.execute(f"INSERT INTO `editors` (news_id, ed_fname, ed_lname, ed_date) VALUES ('{News_int}', '{ed_firstname}', '{ed_lastname}', '{ed_datestarted}');")
            mysql.connection.commit()                                            
            cursor.close()
        return render_template("add.html")
    return render_template("add.html")



@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(f"use newsstand_db;")
        Name = request.form['name']
        ed_firstname = request.form['ed_firstname']
        ed_lastname = request.form['ed_lastname']
        ed_datestarted = request.form['ed_datestarted']
        news_id = cursor.execute(f"SELECT news_id FROM `sites` WHERE '{Name}'")
        mysql.connection.commit()
        cursor.execute(f"UPDATE `editors` SET `ed_date`='{ed_datestarted}' WHERE `news_id`='{news_id}';")
        mysql.connection.commit()
        cursor.close()
        return render_template("add.html")
    return render_template("edit.html")

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(f"use newsstand_db;")
        Name = request.form['name']
        cursor.execute(f" SELECT news_id from `sites` WHERE  news_name = '{Name}';")
        News_id = cursor.fetchone ()
        News_int = News_id["news_id"]
        cursor.execute(f"DELETE from `editors` WHERE news_id = '{News_int}';") 
        mysql.connection.commit()
        cursor.execute(f"DELETE from `sites` WHERE news_id = '{News_int}';")
        mysql.connection.commit()
        cursor.close
        return render_template("delete.html")
    return render_template("delete.html")



@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'

@app.route("/help")
def help():
    return render_template ("help.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
