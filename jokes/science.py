from flask import Blueprint, jsonify
import json
import random

science = Blueprint("science", __name__)

prev = []

with open("jokes.json") as f:
    json_data = json.load(f)

science_data = json_data[0]["jokes"]["science"]

def generate_new_random_number ():
    while True:
        new_number = random.randint(0, 9)
        if new_number not in prev:
            break 
    prev.append(new_number)
    if len(prev) > 3:
        prev.pop(0)
    return new_number

@science.route("/", methods=["GET"])
def jokes ():
    return jsonify(science_data), 200

@science.route("/random-joke", methods=["GET"])
def random_joke ():
    random_number = generate_new_random_number()
    return jsonify(science_data[random_number]), 200