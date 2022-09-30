from openfile import loadFileConfig, headers
from flask import Blueprint, request, jsonify
import requests


result = Blueprint('result', __name__)
dataConfig = loadFileConfig()


"""
--------------------------FLASK - RESULTS------------------------------
"""


@result.get("/result")
def get_results():
    url = dataConfig["url_back"] + "/result"
    response = requests.get(url, headers=headers)
    return jsonify(response.json())


@result.get("/result/<int:id>")
def get_result(id):
    url = dataConfig["url_back"] + "/result/" + id
    response = requests.get(url, headers=headers)
    return jsonify(response.json())


@result.post("/result")
def create_result():
    body = request.get_json()
    url = dataConfig["url_back"] + "/result"
    response = requests.post(url, json=body, headers=headers)
    return jsonify(response.json())


@result.put("/result/<int:id>")
def update_result(id):
    body = request.get_json()
    url = dataConfig["url_back"] + "/result/" + id
    response = requests.put(url, json=body, headers=headers)
    return jsonify(response.json())


@result.delete("/result/<int:id>")
def delete_result(id):
    url = dataConfig["url_back"] + "/result/" + id
    response = requests.delete(url, headers=headers)
    return jsonify(response.json())

