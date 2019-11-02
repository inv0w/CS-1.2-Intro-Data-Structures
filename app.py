from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Return Homepage"""
    return render_template('home.html', msg='Tweet')

if __name__ == '__main__':
    app.run(debug=True)
