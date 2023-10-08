from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Software Development HW-1!!!!"

if __name__=="__main__":
    app.run()
