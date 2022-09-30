from openfile import loadFileConfig, headers
from flask import Blueprint, request, jsonify
import requests, json


report = Blueprint('report', __name__)
dataConfig = loadFileConfig()

@report.route("/report", methods=["PUT"])
def get_report():
    url_security = dataConfig["url_back"] + "/report"
    response = requests.put(url_security, headers=headers)
    return jsonify(response.json())


@report.route("/report/pp", methods=["GET"])
def get_report_party():
    url_security = dataConfig["url_back"] + "/report/pp"
    response = requests.get(url_security, headers=headers)
    return jsonify(response.json())


