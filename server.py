from flask import Flask  # Capital "F" in Flask

app = Flask(__name__)  # Correct object creation

@app.route('/', methods=["GET"])
def root():
    return "this is my web 0.2"  # Must use 'return' inside the function

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)  # Runs on port 4000

