from flask import Flask, Response
from config.server_config import *

app = Flask(__name__)


@app.route("/")
def index():
    f = open("../web/login.html")
    return Response(f.read())


@app.route("/<obj>")
def resp(obj):
    try:
        i = obj.split(".")[1]
        r = READ_DICT[i]
        f = open(f"../web/{obj}", f"{r}")
        data = Response(f.read(), mimetype=f"{CON_DICT[i]}")
        f.close()
    except Exception as e:
        print(e)
        f = open("../web/404.html")
        return Response(f.read())
    else:
        return data


if __name__ == "__main__":
    app.run(debug=True)
