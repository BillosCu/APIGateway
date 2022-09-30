from openfile import loadFileConfig, headers
from flask import Blueprint, request, jsonify
import requests


permiso = Blueprint('permiso', __name__)
dataConfig = loadFileConfig()



"""
--------------------------SPRINGBOOT - PERMISOS------------------------------
"""

@permiso.get("/permiso")
def getpermisos():
    url = dataConfig["url_security"] + '/permiso'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@permiso.post("/permiso")
def crearpermiso():
    data = request.get_json()
    url = dataConfig["url_security"] + '/permiso'
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

@permiso.get("/permiso/<string:id>")
def getpermiso(id):
    url = dataConfig["url_security"] + '/permiso/'+ str(id)
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@permiso.put("/permiso/<string:id>")
def modificarpermiso(id):
    data = request.get_json()
    url = dataConfig["url_security"] + '/permiso/'+str(id)
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@permiso.delete("/permiso/<string:id>")
def eliminarpermiso(id):
    url = dataConfig["url_security"] + '/permiso/' + str(id)
    response = requests.delete(url, headers=headers)
    json = response.json()
    return jsonify(json)
