from flask import Blueprint, jsonify
import json
import random

holiday = Blueprint("holiday", __name__)

with open("jokes.json") as f:
    json_data = json.load(f)

holiday_jokes = json_data[0]["jokes"]["holiday"]

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

@holiday.route("/", methods=["GET"])
def jokes ():
    return jsonify(holiday_jokes), 200

@holiday.route("/random-joke", methods=["GET"])
def random_joke():
    random_number = generate_random_number()
    return jsonify(holiday_jokes[random_number])