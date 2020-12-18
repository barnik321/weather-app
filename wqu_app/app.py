from flask import Flask, render_template, request
from message import greet

app = Flask(__name__)


@app.route('/')
def main():
    ip = request.headers['X-Forwarded-For']
    return render_template('index.html', message=greet(ip))


if __name__ == '__main__':
    app.env = 'development'
    app.run(debug=True)
