#imports
from flask import Flask, render_template, request
import main


app = Flask(__name__) #create flask app



#define app routes
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(main.chat(userText))
if __name__ == "__main__":
    app.run()