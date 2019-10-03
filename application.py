from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
    #return render_template('index.html')
     return render_template('iPhone_X___1.html')

@app.route("/iPhone_X___2.html")
def iPhone_X___2():
     return render_template('iPhone_X___2.html')    

@app.route("/iPhone_X___3.html")
def iPhone_X___3():
     return render_template('iPhone_X___3.html')  
    
@app.route("/iPhone_X___4.html")
def iPhone_X___4():
     return render_template('iPhone_X___4.html')  
    
@app.route("/iPhone_X___5.html")
def iPhone_X___5():
     return render_template('iPhone_X___5.html')  
    
@app.route("/iPhone_X___6.html")
def iPhone_X___6():
     return render_template('iPhone_X___6.html')
    
 @app.route("/iPhone_X___7.html")
def iPhone_X___7():
     return render_template('iPhone_X___7.html')  
    
if __name__ == "__main__":
    app.run()
