from flask import Flask, jsonify
from jokes.kids import kids
from jokes.animals import animals
from jokes.classic import classic
from jokes.food import food
from jokes.holiday import holiday
from jokes.puns import puns
from jokes.science import science
from jokes.sports import sports
from jokes.tech import tech
from jokes.work import work
import json
import random 

app = Flask(__name__)

app.register_blueprint(kids, url_prefix="/kids")
app.register_blueprint(animals, url_prefix="/animals")
app.register_blueprint(classic, url_prefix="/classic")
app.register_blueprint(food, url_prefix="/food")
app.register_blueprint(holiday, url_prefix="/holiday")
app.register_blueprint(puns, url_prefix="/puns")
app.register_blueprint(science, url_prefix="/science")
app.register_blueprint(sports, url_prefix="/sports")
app.register_blueprint(tech, url_prefix="/tech")
app.register_blueprint(work, url_prefix="/work")

with open('jokes.json') as f:
    jokes_data = json.load(f)

prev_category = []
prev_joke = []

def generate_random_joke():
    while True:
        new_joke = random.randint(0, 9)
        new_category = random.randint(0, 9)
        if new_category not in prev_category:
            if new_joke not in prev_joke:
                break
    prev_category.append(new_category)
    prev_joke.append(new_joke)
    if len(prev_category) > 3:
        prev_category.pop(0)
        if len(prev_joke) > 3:
            prev_joke.pop(0)

    category_list = list(jokes_data[0]["jokes"])
    return category_list[new_category], new_joke

print(list(jokes_data[0]["jokes"]))

@app.route("/", methods=["GET"])
def intro():
    return jsonify(jokes_data), 200

@app.route("/random-joke", methods=["GET"])
def random_joke():
    random_category, random_joke_no = generate_random_joke()
    return jsonify(jokes_data[0]["jokes"][random_category][random_joke_no])

if __name__ == "__main__":
    app.run(debug=True)