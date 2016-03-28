from flask import Flask, redirect, url_for, request, abort, jsonify
import json
import os

app = Flask(__name__)


# class users():
#     def __init__(self):
#         self.users = {}


#     def add_user(self, username="johndoe", uni="guc"):

#         self.username = username
#         self.uni = uni

class user():
    def __init__(self, username, uni):
        self.username = username
        self.uni  = uni
        with open("users/%s.json" % username, "w") as f:
            json.dump(self.__dict__, f)
    
    def __str__(self):
        return str(self.__dict__)
    
    def json(self):
        return self.__dict__



@app.route("/")
def index():
    return redirect(url_for("login"))



@app.route("/user/<name>", methods=["POST", "GET", "DELETE"])
def user_action(name):
    if request.method == "POST":
        usi = user(request.form.get("name"), request.form.get("uni"))
        return jsonify(usi.json())
    elif request.methid == "GET":
        if name in os.listdir("users"):
            with open("users/%s.json" % name) as f:
                return jsonify(json.load(f))
        return "SRRY NO USER WITH THAT NAMEi"
    else:
        if name in os.listdir("users"):
            os.remove("users/%s.json" % name)

@app.route("/users")
def users_action():
    if request.method == "GET":
        return jsonify({"users": os.listdir("users")})
    else:
        return abort(405)


@app.errorhandler(405)
def page_not_found(error):
    return "MEthod not allowed", 405


# @app.route("/login", methods=["POST"])
# def get_image():
#    return render_template("home.html")

# @app.route("/input/")
# @app.route("/input/image/<image>", methods=["GET", "POST"])
# def get_image(image):
#     return render_template("home.html", image=image)


#if __name__=="__main__":
app.run(host="0.0.0.0", debug=True)
