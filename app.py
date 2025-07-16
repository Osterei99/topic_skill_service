from flask import Flask, jsonify
import json
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/topics')
def get_topics():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'topics.json')
    with open(data_path, 'r') as f:
        topics = json.load(f)
    return jsonify(topics)

if __name__ == '__main__':
    app.run(debug=True)
