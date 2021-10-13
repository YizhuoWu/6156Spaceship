from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/profile/<username>", methods=["GET"])
def test(username):
    # username = "test_username"
    email = "test_email"

    return jsonify(
        username=username,
        email=email
    )

@app.route("/discover/<username>", methods=["GET","POST"])
def test_discover(username):
    query = request.args.get("query")
    return jsonify(
        username=username,
        query = query
    )

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
