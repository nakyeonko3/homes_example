from flask import Flask, render_template, jsonify

app = Flask(__name__)


# ---------page routing-----------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/mypage")
def mypage():
    return render_template("mypage.html")


@app.route("/odd")
def odd():
    return render_template("odd.html")


@app.route("/help")
def help():
    return render_template("index.html")


# ---------json data------------


@app.route("/test")
def test():
    data = {"test1": [65, 59, 80, 81, 80], "test2": [46, 25, 30]}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=18080)
