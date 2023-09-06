## initialize the flask app and create a simple "hello world" endpoint.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)

# SQLite for the development

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
def hello_world():
	return 'Hello, World!'