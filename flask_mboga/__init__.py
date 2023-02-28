from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = ''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://tam_mysql_user:tam_mysql_pwd@localhost/tam_mysql_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
<<<<<<< HEAD
app.app_context().push() 

=======
app.app_context().push()
>>>>>>> 8035078e11405565f48edaf553c379d058a34dec
from flask_mboga import routes
