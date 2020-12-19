from flask import Flask, render_template
import os
import message

my_app = Flask(__name__)


@my_app.route('/')
def main():
    if os.getenv('DEPLOY') == 'heroku':
        ip = message.get_client_ip_address()
    else:
        ip = message.retrieve_local_ip_adress()
    return render_template('index.html', message=message.greet(ip))


if __name__ == '__main__':
    my_app.env = 'development'
    my_app.run(debug=True)
