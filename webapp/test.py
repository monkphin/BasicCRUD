from flask import Flask, render_template, request

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_HOST'] = 'crud_db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL()

cursor = DbRoutines.mysql.connection.cursor()
cursor.execute(f"INSERT INTO `Firearms` (`SerNumber`, `Make`) VALUES ('45678','Mauser');")
cursor.close()
