"""
Author: Keerthi Prakash R
Date:7th May 2023
Description: IOT Device Management APIs
"""
from flask import Flask, jsonify, Response
from awsiotcore_functions.awsiotcore_functions import ThingManager

app = Flask(__name__)


@app.route("/registerdevice")
def register_device() -> Response:
    """
    Registers a new device.
    """
    try:
        thing_manager = ThingManager()
        thing_obj = thing_manager.create_thing()
        response_data = jsonify(thing_obj.to_dict())
        response_data.headers.add('Content-Type', 'application/json')
        return response_data
    # TODO: Catch specific exceptions, log and return meaningful error
    #   in the sample code below this is not advised for production
    except Exception as error_object:
        error_message = str(error_object)
        response_data = jsonify({'error': error_message})
        response_data.status_code = 500
        return response_data


@app.route("/deletedevice")
def delete_device() -> Response:
    """
    Delete device from iot core
    """
    try:
        thing_manager = ThingManager()
        result = thing_manager.delete_thing("gateway_1")
        response_data = jsonify(result)
        response_data.headers.add('Content-Type', 'application/json')
        return response_data
    # TODO: Catch specific exceptions, log and return meaningful error
    #   in the sample code below this is not advised for production
    except Exception as error_object:
        error_message = str(error_object)
        response_data = jsonify({'error': error_message})
        response_data.status_code = 500
        return response_data


if __name__ == '__main__':
    app.run()
