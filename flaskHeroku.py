# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask import render_template


import sys
import json

from flask.views import MethodView


app= Flask(__name__)

#@app.route("/")
#def hello(name):
#  return render_template("home.html", name="visitor")


@app.route("/<string:name>")
def hello(name = "visitor"):
  return render_template("home.html", name=name)


if __name__ == '__main__':
  app.run(port=5300,debug=True)

