from flask import Flask, render_template, jsonify, request
import requests
from flask_cors import CORS
from db import is_valid_course

app = Flask(__name__)
CORS(app)

@app.route("/get_courses", methods = ["GET", "POST"])
def get_courses():
    if request.method == "GET":
        return jsonify("hello")
    else:
        code = request.json["courseCode"]
        return jsonify(is_valid_course(code))

@app.route("/get_papers", method = ["GET", "POST"])
def get_papers():
    if request.method == "POST":
        code = request.json["courseCode"]
