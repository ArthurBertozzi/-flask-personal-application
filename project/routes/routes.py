from flask import render_template, redirect, url_for, flash, request, abort
from project import app


@app.route('/')
def hello():
    return render_template('homepage.html')
