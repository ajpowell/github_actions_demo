from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()  # Take environment variables from .env

app = Flask(__name__)


@app.route('/')
def return_root():
    return 'Hello there', 200


@app.route('/<random_string>')
def return_backwards_string(random_string):
    return "".join(reversed(random_string)), 200


@app.route('/get-mode')
def get_mode():
    return os.environ.get('MODE'), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
