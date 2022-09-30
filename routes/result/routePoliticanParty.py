from flask import Blueprint, request, jsonify
from openfile import loadFileConfig, headers
import requests

pp = Blueprint('pp', __name__)

dataConfig = loadFileConfig()

"""
--------------------------FLASK - POLITICAN PARTY------------------------------
"""


@pp.get("/pp")
def get_parties():
    url = dataConfig["url_back"] + "/pp"
    response = requests.get(url, headers=headers)
    return jsonify(response.json())


@pp.get("/pp/<int:id>")
def get_party(id):
    url = dataConfig["url_back"] + "/pp/" + id
    response = requests.get(url, headers=headers)
    return jsonify(response.json())


@pp.post("/pp")
def create_party():
    body = request.get_json()
    url = dataConfig["url_back"] + "/pp"
    response = requests.post(url, json=body, headers=headers)
    return jsonify(response.json())


@pp.put("/pp/<int:id>")
def update_party(id):
    body = request.get_json()
    url = dataConfig["url_back"] + "/pp/" + id
    response = requests.put(url, json=body, headers=headers)
    return jsonify(response.json())


@pp.delete("/pp/<int:id>")
def delete_party(id):
    url = dataConfig["url_back"] + "/pp/" + id
    response = requests.delete(url, headers=headers)
    return jsonify(response.json())

