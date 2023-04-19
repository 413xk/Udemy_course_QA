from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({'message': 'Hello, world!'}) # convert dictionary to string for flask. Flask cannot work with dict


if __name__ == '__main__':
    app.run()
