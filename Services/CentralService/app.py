from flask import Flask, request, jsonify
import requests


app = Flask(__name__)

# Registry of services
services = {}

@app.route('/services', methods=['GET'])
def list_services():
    return jsonify(list(services.values()))

@app.route('/services', methods=['POST'])
def register_service():
    data = request.json
    services[data['name']] = data['url']
    return jsonify({"message": "Service registered successfully"}), 200


@app.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.json
    service_name = data['service']
    text = data['text']

    if service_name not in services:
        return jsonify({"error": "Requested service does not exist"}), 404

    response = requests.post(services[service_name], json={"text": text})
    return jsonify(response.json())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
