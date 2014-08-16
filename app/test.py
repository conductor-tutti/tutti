from flask import jsonify, request, render_template
from app import app

@app.route("/")
def index():
    return render_template("test.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        input_first = request.form.get("input_first", 0, type=int)
        input_second = request.form.get("input_second", 0, type=int)
        return jsonify(result = input_first + input_second)
    else:
        return "POST request only"