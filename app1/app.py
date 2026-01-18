from flask import Flask
app = Flask(__name__)

@app.route("/app1")
def home():
    return "Hello from APP-1 🚀"

@app.route("/")
def root():
    return "APP-1 root"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

