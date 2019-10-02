from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
    #return render_template('index.html')
     return render_template('iPhone_X___1.html')
if __name__ == "__main__":
    app.run()
