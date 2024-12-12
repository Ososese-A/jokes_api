from flask import Blueprint, jsonify
import json
import random

sports = Blueprint("sports", __name__)

with open("jokes.json") as f:
    jokes_data = json.load(f)

sports_jokes = jokes_data[0]["jokes"]["sports"]

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


@sports.route("/", methods=["GET"])
def jokes ():
    return jsonify(sports_jokes), 200

@sports.route("/random-joke", methods=["GET"])
def random_joke ():
    random_number = generate_random_number()
    return jsonify(sports_jokes[random_number]), 200