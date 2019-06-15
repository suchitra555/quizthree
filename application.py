from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello suchitra suchitra suchitra suchitra World123"
