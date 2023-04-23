from flask import Flask, render_template

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True, port=18080)
