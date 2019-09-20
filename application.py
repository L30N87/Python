from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Marcela Lopez!"
def hello2():
    return "Carlos Bosmediano!"
    return "Geovanny Ruiz!"
