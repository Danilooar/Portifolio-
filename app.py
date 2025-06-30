import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # usa a porta do ambiente ou 5000 como padrão
    app.run(host="0.0.0.0", port=port, debug=True)
