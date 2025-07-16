from flask import Flask, jsonify
import json
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello from Topic & Skill Service!"

@app.route('/topics')
def get_topics():
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'topics.json')
    
    try:
        with open(data_path, 'r') as f:
            topics = json.load(f)
        return jsonify(topics)
    except json.JSONDecodeError:
        print(f"Fehler beim Dekodieren der JSON-Datei: {data_path}. Bitte JSON-Syntax überprüfen!")
        return []
    except Exception as e:
        print(f"Ein unbekannter Fehler ist aufgetreten: {e}")
        return []


if __name__ == '__main__':
    app.run(debug=True,port=5000)
