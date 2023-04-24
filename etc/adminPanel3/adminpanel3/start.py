from flask import Flask, send_from_directory


app = Flask(__name__, static_folder="/static", template_folder="/templates")


@app.route("/")
def index():
    return send_from_directory("static", "/templates/index.html")


app.run(debug=True, host="0.0.0.0")
