from flask import Blueprint, jsonify
import json
import random

kids = Blueprint("kids", __name__)

with open("jokes.json") as f:
    json_data = json.load(f)

kids_jokes = json_data[0]["jokes"]["kids"]

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

@kids.route("/", methods=["GET"])
def jokes ():
    return jsonify(kids_jokes), 200

@kids.route("/random-joke", methods=["GET"])
def random_joke():
    random_number = generate_random_number()
    return jsonify(kids_jokes[random_number]), 200