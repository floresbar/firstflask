from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def hello_world():
    return "<p>Hello, from TechLabs!</p>"

wines = [
    {"id": 0, "alcohol": 8, "quality": 10},
    {"id": 1, "alcohol": 12, "quality": 8},
    {"id": 2, "alcohol": 10.5, "quality": 9},
]

@app.route("/api/wines/all", methods=["GET"])
def return_all():
    return jsonify(wines)

@app.route("/api/wines", methods=["GET"])
def get_wine_by_id():
    if "id" in request.args:
        id = int(request.args["id"])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for wine in wines:
        if wine["id"] == id:
            results.append(wine)

    return jsonify(results)