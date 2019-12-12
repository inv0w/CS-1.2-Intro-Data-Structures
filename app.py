from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from Code.markov_chain import Markov
from twitter import tweet
from __future__ import unicode_literals
import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Tweet-Generator')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
favorites = db.favorites

app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    text = 'Code/textdocs/Scarletletter.txt'
    markov = Markov(text, 20)
    sentence = markov.main()
    return render_template('home.html', tweet=sentence)

@app.route('/tweet', methods=['POST'])
def tweets():
    status = request.form['sentence']
    tweet(status)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
