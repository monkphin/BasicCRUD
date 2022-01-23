from distutils.log import debug
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename #Needed for future functionality
from werkzeug.datastructures import  FileStorage #Needed for future functionality
import os # needed for future functionality


app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'crud_db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

app.testing = True


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
    site_list = cursor.fetchall()
    cursor.close()

    return render_template("index.html", len = len(site_list), site_list = site_list)



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


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        Name= request.form['name']
        Site = request.form['url']
        cursor = mysql.connection.cursor()
        cursor.execute(f"use newsstand_db;") 
        cursor.execute(f"UPDATE `sites` SET `news_name` = '{Name}', `news_url` = '{Site}' WHERE `sites`.`news_id` = '{id}'") 
        mysql.connection.commit()                                            
        cursor.close()
    return render_template('/edit.html', id=id)


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(f"use newsstand_db;")  
        cursor.execute(f"SELECT news_name FROM sites WHERE news_id = {'id'}") 
        list = cursor.fetchall()
        cursor.close
        cursor = mysql.connection.cursor()
        cursor.execute(f"use newsstand_db;") 
        cursor.execute(f"DELETE FROM `sites` WHERE `sites`.`news_id` = {'id'}'")
        mysql.connection.commit()                                            
        cursor.close()
    return render_template('/delete.html', list=list, id=id)

#to iumplement - for uploading of custom images. 
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
