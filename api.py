from flask import Flask, jsonify
from scraper import course_search
import json

app = Flask(__name__)

@app.route("/")
def wefgew():
    return "aymane"

@app.route("/query/<query>")
def search(query):
    #res = course_search(query)

    res = [{"id": "24", "name": "qwerw", "description": "afse", "professors": "we", "contents": "sgjo", "objectives": "fea"}]
    res.append(res[0])
    res[1]["id"] = "aymane"
    response = jsonify(res)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response