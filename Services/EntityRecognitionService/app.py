from flask import Flask, request, jsonify

app = Flask(__name__)

# entity_recognition
@app.route('/recognize', methods=['POST'])
def recognize_entities():
    data = request.json
    text = data.get("text", "")

    entities = identify_entities(text)

    return jsonify({"entities": entities})

def identify_entities(text):
    entities = []
    if "Boston" in text:
        entities.append({"entity": "Boston", "type": "Location"})
    if "Lendbuzz" in text:
        entities.append({"entity": "Lendbuzz", "type": "Organization"})

    return entities

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
