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
@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "GET":
        global r
        return r
    elif request.method == "POST":
        global task_id
        data = request.json
        task_id += 1
        r["title"] = data["title"]
        r["description"] = data["description"]
        r["task_id"] = task_id
        return (r, 200, {"content-type": "application/json"})


@app.route("/task/<int:task_id>", methods=["GET", "POST"])
def get_task(task_id):
    if request.method == "GET":
        title = request.args.get["title"]
        description = request.args.get["description"]
        return f"task number {task_id}"

    elif request.method == "POST":
        data = request.json
        r["title"] = data["title"]
        r["description"] = data["description"]
        return (r, 200, {"content-type": "application/json"})


# POST ->
# {
#     "title": "Покормить кота",
#     "description": "Надо купить ему Whiskas или Purina, а то будет опять злой"
# }

# # return: <- f'{
#     "description": "Надо купить ему Whiskas или Purina, а то будет опять
#     злой",
#     "task_id": 1,
#     "title": "Покормить кота"
# }'

if __name__ == "__main__":
    app.run(debug=True, port=5000)
