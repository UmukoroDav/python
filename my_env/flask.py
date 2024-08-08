from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h3>elcome to my web aplication</h3>'