from flask import Flask

from _app import app
import _redirecting

@app.route('/')
def func():
    _redirecting.redirecting()