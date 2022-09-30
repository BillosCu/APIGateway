from openfile import loadFileConfig, headers
from flask import Blueprint, request, jsonify
import requests

rol = Blueprint('rol', __name__)
dataConfig = loadFileConfig()


"""
--------------------------SPRINGBOOT - ROLES------------------------------
"""

@rol.get("/rol")
def getroles():
    url = dataConfig["url_security"] + '/rol'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@rol.post("/rol")
def crearrol():
    data = request.get_json()
    url = dataConfig["url_security"] + '/rol'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

@rol.get("/rol/<string:id>")
def getrol(id):
    url = dataConfig["url_security"] + '/rol/'+str(id)
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@rol.put("/rol/<string:id>")
def modificarrol(id):
    data = request.get_json()
    url = dataConfig["url_security"] + '/rol/'+str(id)
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@rol.delete("/rol/<string:id>")
def eliminarrol(id):
    url = dataConfig["url_security"] + '/rol/' + str(id)
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)
