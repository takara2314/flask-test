import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def rootFunc():
    if request.method == "GET":
        return "GETされました！"
    elif request.method == "POST":
        return "POSTされました！"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=os.getenv("PORT"))