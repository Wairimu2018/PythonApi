from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Wairimu Kuria",
        # "DOB": "1993-10-15",
        "email": "mimokuria@gmail.com"
    }

# query parameter

    extra = request.args.get("extra")
    if extra:
       user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
   
    data = request.get_json()

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8000, debug=True)