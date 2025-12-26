from flask import Flask, request, redirect
import random

app = Flask(__name__)
SCORE = 0


@app.route("/", methods=["GET", "POST"])
def index():
    global SCORE
    if request.method == "GET":
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        z = x * y
        L = [z, random.randint(4, 81), random.randint(4, 81), random.randint(4, 81)]
        random.shuffle(L)
        return (
            f"Your score is {SCORE}"
            f"<h1>{x}*{y}=?</h1>"
            f"<a href=/{"correct" if L[0]==z else "incorrect"}>{L[0]}</a><br>"
            f"<a href=/{"correct" if L[1]==z else "incorrect"}>{L[1]}</a><br>"
            f"<a href=/{"correct" if L[2]==z else "incorrect"}>{L[2]}</a><br>"
            f"<a href=/{"correct" if L[3]==z else "incorrect"}>{L[3]}</a><br>"
        )

    else:
        data = request.json
        # return f"name: {data['name']} <br" f"surname: {data['surname']}"
        r = dict()
        r["name"] = data["name"]
        r["surname"] = data["surname"]
        return (r, 200, {"content-type": "application/json"})


@app.route("/test/hello")
def test_hello():
    return "<h3>I asked for test/hello page</h3>"


@app.route("/error")
def error():
    raise NotImplementedError
    return "<h1>You asked for wrong page!</h1>"


@app.route("/correct")
def correct():
    global SCORE
    SCORE += 1
    return redirect("/")


@app.route("/incorrect")
def incorrect():
    global SCORE
    SCORE -= 1
    return redirect("/")


@app.route("/user/<int:user_id>")
def get_user(user_id):
    key = request.args.get("key")  # чтобы получить данные из самой строки ЮРЛ
    value = request.args.get("value")
    return f"User number {user_id}. {key}: {value}"


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return """<form method="POST" action="">
        Name <input types="text" name="name">
        Surname <input type="text" name='surname'>
        <input type='submit'>
        </form> """
    else:
        name = request.form["name"]
        surname = request.form["surname"]
        return f"Hello {name} {surname}"


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
