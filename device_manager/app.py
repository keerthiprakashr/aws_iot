"""
Device Management APIs for AWS IOT.

Author: Keerthi Prakash R.

Date:7th May 2023

Description: IOT Device Management APIs

"""
from flask import Flask, jsonify, Response, request
from awsiotcore_functions.awsiotcore_functions import ThingManager

app = Flask(__name__)


@app.route("/registerdevice", methods=['GET'])
def register_device() -> Response:
    """Register a new device."""
    try:
        name = request.args.get("thingname", "gateway_1")
        thing_manager = ThingManager()
        thing_obj = thing_manager.create_thing(name)
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


@app.route("/deletedevice",  methods=['GET'])
def delete_device() -> Response:
    """Delete device from iot core."""
    try:
        name = request.args.get("thingname", "gateway_1")
        thing_manager = ThingManager()
        result = thing_manager.delete_thing(name)
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
