from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = '611e204927d4e611f723b1935726c350a1c05ade'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://TAM_MYSQL_USER:TAM_MYSQL_PWD@TAM_MYSQL_HOST/TAM_MYSQL_DB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push() 

from flask_mboga import routes
