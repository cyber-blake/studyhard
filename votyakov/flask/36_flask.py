from flask import Flask, request, redirect
import random
import os

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
r = dict()
task_id = 0


@app.route("/")
def index():
    if request.method == "GET":
        return f'<h1 align="center"> Hello weeaboo!</h1> <form action="/random-quote" method="GET"><input type="submit"value="Получить цитату"></form>'


# * 1
@app.route("/random-quote")
def random_quote():
    file_path = os.path.join(BASE_DIR, "quotes.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        List = f.readlines()
    return random.choice(List)


# * 2
@app.route("/api/convert-temperature", methods=["GET", "POST"])
def api_convert():
    if request.method == "GET":
        return f"<h2>This is an API site package module</h2> <h3>send POST to convert Temp</h3>"
    elif request.method == "POST":
        data = request.json
        C = int(data["celsius"])
        F = C * 1.8 + 32
        return {"fahrenheit": F}


# * 3
r = dict()
big_dict = dict()


@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    global r
    global big_dict
    if request.method == "GET":
        return r
    elif request.method == "POST":
        global task_id
        data = request.json
        task_id += 1
        r["title"] = data["title"]
        r["description"] = data["description"]
        r["task_id"] = task_id
        big_dict.update({"task_id": r["task_id"]})
        return (r, 200, {"content-type": "application/json"})


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def get_task(task_id):
    global r
    # data = request.json
    r.pop("task_id")
    return (
        {"message": "Задача успешно удалена"},
        200,
        {"content-type": "application/json"},
    )


@app.route("/debug", methods=["POST"])
def debug_request():
    print("=== HEADERS ===")
    print(dict(request.headers))

    print("=== JSON DATA ===")
    print(
        request.get_json(silent=True)
    )  # silent=True чтобы не было ошибок если не JSON
    return "<h1>alles normales</h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
