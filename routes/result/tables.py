from openfile import loadFileConfig, headers
from flask import Blueprint, request, jsonify
import requests

table = Blueprint('table', __name__)

dataConfig = loadFileConfig()

"""
--------------------------FLASK - TABLE------------------------------
"""


@table.get("/table")
def get_tables():
    url = dataConfig["url_back"] + "/table"
    response = requests.get(url, headers=headers)
    return jsonify(response.json())


@table.get("/table/<int:id>")
def get_table(id):
    url = dataConfig["url_back"] + "/table/" + id
    response = requests.get(url, headers=headers)
    return jsonify(response.json())


@table.post("/table")
def create_table():
    body = request.get_json()
    url = dataConfig["url_back"] + "/table"
    response = requests.post(url, json=body, headers=headers)
    return jsonify(response.json())


@table.put("/table/<int:id>")
def update_table(id):
    body = request.get_json()
    url = dataConfig["url_back"] + "/table/" + id
    response = requests.put(url, json=body, headers=headers)
    return jsonify(response.json())


@table.delete("/table/<int:id>")
def delete_table(id):
    url = dataConfig["url_back"] + "/table/" + id
    response = requests.delete(url, headers=headers)
    return jsonify(response.json())

