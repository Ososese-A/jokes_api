from flask import Blueprint, jsonify
import json
import random

classic = Blueprint("classic", __name__)

with open("jokes.json") as f:
    jokes_data = json.load(f)

classic_jokes = jokes_data[0]["jokes"]["classic"]

prev = []

def generate_random_number ():
    while True:
        new_number = random.randint(0, 9)
        if new_number not in prev:
            break
    prev.append(new_number)
    if len(prev) > 3:
        prev.pop(0)
    return new_number

@classic.route("/", methods=["GET"])
def jokes ():
    return jsonify(classic_jokes), 200

@classic.route("/random-joke", methods=["GET"])
def random_joke():
    random_number = generate_random_number()
    return jsonify(classic_jokes[random_number])