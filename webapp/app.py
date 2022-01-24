from distutils.log import debug
from flask import Flask, render_template, request, redirect
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
app.config['MYSQL_DB'] = 'newsstand_db'

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
            Name = request.form['name']
            Site = request.form['url']
            ed_firstname = request.form['ed_firstname']
            ed_lastname = request.form['ed_lastname']
            ed_datestarted = request.form['ed_datestarted']
            cursor.execute(f"INSERT INTO `sites`  (`news_name`, `news_url`) VALUES ('{Name}','{Site}');")
            mysql.connection.commit()     

            '''     Begin hacky method to populate the foreign key in editors table     '''      
            cursor.execute(f" SELECT news_id from `sites` WHERE  news_name = '{Name}'")
            News_id = cursor.fetchone ()
            News_int = News_id["news_id"]
            cursor.execute(f"INSERT INTO `editors` (news_id, ed_fname, ed_lname, ed_date) VALUES ('{News_int}', '{ed_firstname}', '{ed_lastname}', '{ed_datestarted}');")
            mysql.connection.commit()                                            
            cursor.close()
            '''     End hacky method to populate the foreign key in editors table      '''      

        return redirect('/home')

    return render_template("add.html")


@app.route('/sites/<id>/edit', methods=['GET', 'POST'])
def edit(id):
 #GET is to render out put into fields to show what you're currently editing. Currently not working as expected.  
    if request.method == 'GET':
       
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM `sites` WHERE `sites`.`news_id` = '{id}';")
        local_edit_list = cursor.fetchall()
     

        return render_template('/edit.html', id=id, edit_list=local_edit_list)

    if request.method == 'POST':

        new_site_url = request.form['new_name']
        new_site_name = request.form['new_url']
        ed_fname = request.form['ed_f']
        ed_lname = request.form['ed_l']
        ed_date = request.form['ed_d']
        cursor = mysql.connection.cursor()
        cursor.execute(f"UPDATE `sites` SET `news_name`='{new_site_name}', `news_url`='{new_site_url}' WHERE `sites`.`news_id`='{id}';") 
        cursor.execute(f"UPDATE `editors` SET `ed_fname`='{ed_fname}', `ed_lname`='{ed_lname}', `ed_date`='{ed_date}' WHERE `editors`.`news_id`='{id}';") 
        mysql.connection.commit()                                          
        cursor.close()

        return redirect('/home')
    



@app.route('/sites/<id>/delete', methods=['GET', 'POST'])
def delete(id):

    if request.method == 'GET':

        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM `sites` WHERE `sites`.`news_id` = '{id}';")
        local_delete_list = cursor.fetchall()
     


        return render_template('/delete.html', id=id, delete_list=local_delete_list)

    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(f"DELETE FROM `editors` WHERE `news_id` = '{id}';")
        cursor.execute(f"DELETE FROM `sites` WHERE `sites`.`news_id` = '{id}';")
        mysql.connection.commit()                                          
        cursor.close()

        return redirect('/home')
    
'''
@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():

'''

@app.route("/help")
def help():
    return render_template ("help.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
