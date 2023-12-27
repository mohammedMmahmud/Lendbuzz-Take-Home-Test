from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/count', methods=['POST'])
def count():
    data = request.json
    text = data.get("text", "")
    word_count = len(text.split())

    return jsonify({"word_count": word_count})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
