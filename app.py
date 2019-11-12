from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from Code.dictogram import read_file
from Code.markov_chain import create_sentence, walk
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Tweet-Generator')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
favorites = db.favorites

app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    text = 'Code/textdocs/AirplanesAndSubs.txt'
    words = read_file(text)
    sentence = create_sentence(walk(words, 15))
    return render_template('home.html', tweet=sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
