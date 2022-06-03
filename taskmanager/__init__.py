import os
from flask import flask
from flask_sqlalchemy import sqlalchemy
if os.path.exists("env.py"):
    import env   #noqa

app = flask(__name__)    
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = sqlalchemy(app)

from taskmanager import routes  #noqa
