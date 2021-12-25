# import modules
from area import area_to_acre
from flask import Flask, jsonify, request

# instantiate Flask object
app = Flask(__name__)

# endpoints


@app.route("/", methods=['GET', 'POST'])
def get_area():
    '''
    A Flask app to take input and invoke area module to process input parameters to return the area in acres.
    '''

    packet = request.get_json(force=True)
    length = packet['length']
    width = packet['width']

    # instantiate area object to evaluate input
    area = area_to_acre(length, width)

    return jsonify({"area_in_acre": area, "input": packet})
