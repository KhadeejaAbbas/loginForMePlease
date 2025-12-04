from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # This allows your frontend to send requests from any origin

# Store attempts in memory (for demo)
attempts = []

@app.route('/api/attempts', methods=['POST'])
def save_attempt():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Invalid format'}), 400

    attempt = {
        'name': data['name'],
        'timestamp': data.get('timestamp', datetime.utcnow().isoformat())
    }
    attempts.append(attempt)
    return jsonify({'status': 'saved', 'attempt': attempt}), 200

@app.route('/api/attempts', methods=['GET'])
def get_attempts():
    return jsonify(attempts), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
