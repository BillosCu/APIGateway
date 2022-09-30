from flask import Blueprint, request, jsonify
from openfile import loadFileConfig, headers
import requests


users = Blueprint('users', __name__)
dataConfig = loadFileConfig()

"""
--------------------------SPRINGBOOT - USUARIOS------------------------------
"""

@users.get("/users")
def getusers():
    url = dataConfig["url_security"] + '/users'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@users.post("/users")
def crearusers():
    data = request.get_json()
    url = dataConfig["url_security"] + '/users'
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@users.get("/users/<string:id>")
def getuser(id):
    url = dataConfig["url_security"] + '/users/'+str(id)
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@users.put("/users/<string:id>")
def modificarusers(id):
    data = request.get_json()
    url = dataConfig["url_security"] + '/users/'+str(id)
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@users.delete("/users/<string:id>")
def eliminarEstudiante(id):
    url = dataConfig["url_security"] + '/users/' + str(id)
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)

@users.post("/users/validacion")
def validarusers():
    data = request.get_json()
    url_security = dataConfig["url-security"] + "/users/validacion"
    response = requests.post(url_security, json=data, headers=headers)
    return jsonify(response.json())
