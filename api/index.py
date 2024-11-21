from flask import Flask

app = Flask(__name__)
def text(t:str):
    return t
@app.route('/')
def home():
    return text("him")

@app.route('/about')
def about():
    return 'About'
