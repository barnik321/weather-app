from flask import Flask, render_template
import os
import ip as IP
import greeting

my_app = Flask(__name__)


@my_app.route('/')
def main():
    if os.getenv('DEPLOY') == 'heroku':
        ip = IP.get_client_ip_address()
    else:
        ip = IP.retrieve_local_ip_adress()

    results = dict(zip(['place', 'temp', 'org'], greeting.greet(ip)))
    return render_template('index.html', **results)


if __name__ == '__main__':
    my_app.env = 'development'
    my_app.run(debug=True)
