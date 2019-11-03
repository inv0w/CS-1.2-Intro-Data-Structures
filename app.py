from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from Code.sample import get_sentence
from Code.analyze_words import histogram_dict
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/CS-1.2-Intro-Data-Structures')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()

app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    text = 'Code/textdocs/AirplanesAndSubs.txt'
    histogram = histogram_dict(text)
    sentence = get_sentence(histogram, 20)
    return render_template('home.html', tweet=sentence)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
