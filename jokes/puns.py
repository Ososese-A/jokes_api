from flask import Blueprint, jsonify
import json
import random

puns = Blueprint("puns", __name__)

with open("jokes.json") as f:
    json_data = json.load(f)

list_of_puns = json_data[0]["jokes"]["puns"]

prev = []

def generate_unique_random_number():
    while True:
        new_number = random.randint(0, 9)
        if new_number not in prev:
            break
    prev.append(new_number)
    if len(prev) > 3:
        prev.pop(0)
    return new_number

@puns.route("/", methods=["GET"])
def jokes ():
    return "random puns", 200

@puns.route("/random-pun", methods=["GET"])
def random_pun ():
    random_number = generate_unique_random_number()
    return jsonify(list_of_puns[random_number]), 200