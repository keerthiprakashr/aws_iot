"""
Author: Keerthi Prakash R
Date: 
Description: IOT Device Management APIs
"""
from flask import Flask

app = Flask(__name__)


@app.route("/firstbreath")
def device_first_breath() -> str:
    """
    activate device device
    """
    return "Revieved the first  breath"


@app.route("/registerdevice")
def device_register() -> str:
    """
    register device
    """
    return "registered device"


@app.route("/getCertificates")
def get_device_certificates() -> str:
    """
    return device certificate
    """
    return "returing certificates"
