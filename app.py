from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
from flask_jwt_extended import create_access_token, JWTManager, get_jwt_identity, verify_jwt_in_request
import json
import datetime
import re
import requests
from openfile import loadFileConfig, headers
from routes.result.routePoliticanParty import pp
from routes.result.candidates import candidate
from routes.result.results import result
from routes.result.tables import table

from routes.security.users import users
from routes.security.rol import rol
from routes.security.permiso import permiso
from routes.security.permisorol import permisosrol

app = Flask(__name__)
cors = CORS(app)


info = loadFileConfig()

denegado = {"mensaje": "Permiso denegado"}


app.register_blueprint(pp)
app.register_blueprint(result)
app.register_blueprint(candidate)
app.register_blueprint(table)

app.register_blueprint(users)
app.register_blueprint(rol)
app.register_blueprint(permiso)
app.register_blueprint(permisosrol)

def format_url():
    parts = request.path.split("/")
    url = request.path
    for part in parts:
        if re.search('\\d', part):
            url = url.replace(part, "?")
    return url

@app.before_request
def before_request_callback():
    request.path = format_url()
    excludeRoutes = ["/login", "/"]
    #Token
    if request.path not in excludeRoutes:
        if not verify_jwt_in_request():
            return jsonify(denegado), 401

        #Roles y permisos
        user = get_jwt_identity()
        if user['rol'] is None:
            return jsonify(denegado), 401
        else:
            rol_id = user['rol']['_id']
            route = format_url()
            method = request.method
            has_permission = validarPermiso(rol_id, route, method)
            if not has_permission:
                return jsonify(denegado), 401


def validarPermiso(rol_id, endPoint, metodo):
    url = info['url_security']+"/permisos-rol/validar/rol/" + str(rol_id)
    tienePermiso = False
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.get(url, json=body, headers=headers)
    try:
        data = response.json()
        if("_id" in data):
            tienePermiso = True
    except:
        pass
    return tienePermiso



app.config["JWT_SECRET_KEY"] = info['jwt-key']
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def login():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    data = request.get_json()
    url = info["url_security"] + "/users/validacion"
    response = requests.post(url, json=data, headers=headers)
    code = response.status_code

    if code == 401:
        return jsonify({"msg": "Usuario o contraseña incorrectos"}), 401
    elif code == 500:
        return jsonify({"msg": "Error inesperado"}), 500
    if code == 200:
        user = response.json()
        expires = datetime.timedelta(seconds=60 * 60 * 24)
        access_token = create_access_token(identity=user, expires_delta=expires)
        return jsonify({"token": access_token, "user_id": user["_id"]})
    else:
        response = response.text
        res = json.loads(response)
        return jsonify({'mensaje': res['mensaje']}), code



@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)




if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-apigateway"]+":" + str(dataConfig["port-apigateway"]))
    serve(app, host=dataConfig["url-apigateway"],port=dataConfig["port-apigateway"])



