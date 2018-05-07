from app_name import app, db
from flask import render_template


@app.route('/')
def hello():
    return "Hello World!"
