from openfile import loadFileConfig, headers
from flask import Blueprint, request, jsonify
import requests

permisosrol = Blueprint('permisos-rol', __name__)
dataConfig = loadFileConfig()


"""
--------------------------SPRINGBOOT - PERMISOS/ROL------------------------------
"""

@permisosrol.get("/permisos-rol")
def getpermisosroles():
    url = dataConfig["url_security"] + '/permisos-rol'
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@permisosrol.post("/permisos-rol/rol/<string:id_rol>/permiso/<string:id_permiso>")
def crearpermisosrol(id_rol, id_permiso):
    data = request.get_json()
    url = dataConfig["url_security"] + '/permisos-rol/rol' + str(id_rol) + "/permiso/" + str(id_permiso)
    response = requests.post(url, headers=headers,json=data)
    json = response.json()
    return jsonify(json)

@permisosrol.get("/permisos-rol/<string:id>")
def getpermisorol(id):
    url = dataConfig["url_security"] + '/permisos-rol/' + str(id)
    response = requests.get(url, headers=headers)
    json = response.json()
    return jsonify(json)

@permisosrol.put("/permisos-rol/<string:id>/rol/<string:id_rol>/permiso/<string:id_permiso>")
def modificarpermisosrol(id, id_rol, id_permiso):
    data = request.get_json()
    url = dataConfig["url_security"] + '/permisos-rol/' + str(id) + "/rol/" + str(id_rol) + "/permiso/" + str(id_permiso)
    response = requests.put(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)

@permisosrol.post("/permisos-rol/validar/rol/<string:id_rol>")
def validarpermisorol(id_rol):
    data = request.get_json()
    url = dataConfig["url_security"] + '/permisos-rol/validar/rol/' + str(id_rol)
    response = requests.post(url, headers=headers, json=data)
    json = response.json()
    return jsonify(json)






