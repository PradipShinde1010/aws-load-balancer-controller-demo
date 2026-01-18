from flask import Flask
app = Flask(__name__)

@app.route("/app2")
def home():
    return "Hello from APP-2 🔥"

@app.route("/")
def root():
    return "APP-2 root"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

