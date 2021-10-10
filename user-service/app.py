from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/profile")
def test():
    username = "test_username"
    email = "test_email"

    return jsonify(
        username=username,
        email=email
    )

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
