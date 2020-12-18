from flask import Flask, render_template, request
from message import greet

my_app = Flask(__name__)


@my_app.route('/')
def main():
    ip = request.headers['X-Forwarded-For']
    return render_template('index.html', message=greet(ip))


if __name__ == '__main__':
    my_app.env = 'development'
    my_app.run(debug=True)
