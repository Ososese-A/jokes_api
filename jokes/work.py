from flask import Blueprint, jsonify
import json
import random

work = Blueprint("work", __name__)

with open("jokes.json") as f:
    json_data = json.load(f)

work_jokes = json_data[0]["jokes"]["work"]

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

@work.route("/", methods=["GET"])
def jokes ():
    return "random work jokes", 200

@work.route("/random-joke", methods=["GET"])
def random_joke ():
    random_number = generate_random_number()
    return jsonify(work_jokes[random_number]), 200