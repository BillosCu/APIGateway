from openfile import loadFileConfig, headers
from flask import Blueprint, request, jsonify
import requests, json

candidate = Blueprint('candidate', __name__)
dataConfig = loadFileConfig()

"""
--------------------------FLASK - CANDIDATES------------------------------
"""


@candidate.get("/candidate")
def get_candidates():
    url_security = dataConfig["url_back"] + "/candidate"
    response = requests.get(url_security, headers=headers)
    return jsonify(response.json())


@candidate.get("/candidate/<int:id>")
def get_candidate(id):
    url_security = dataConfig["url_backs"] + "/candidate/" + id
    response = requests.get(url_security, headers=headers)
    return jsonify(response.json())


@candidate.post("/candidate")
def create_candidate():
    body = request.get_json()
    url_security = dataConfig["url_back"] + "/candidate"
    response = requests.post(url_security, json=body, headers=headers)
    return jsonify(response.json())


@candidate.put("/candidate/<int:id>")
def update_candidate(id):
    body = request.get_json()
    url_security = dataConfig["url_back"] + "/candidate/"  + id
    response = requests.put(url_security, json=body, headers=headers)
    return jsonify(response.json())


@candidate.delete("/candidate/<int:id>")
def delete_candidate(id):
    url_security = dataConfig["url_back"] + "/candidate/" + id
    response = requests.delete(url_security, headers=headers)
    return jsonify(response.json())

