from flask import Flask, request, jsonify

app = Flask(__name__)

# sentiment_analysis
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get("text", "")

    sentiment = determine_sentiment(text)

    return jsonify({"sentiment": sentiment})

# Basic sentiment analysis logic
def determine_sentiment(text):
    positive_words = ['good', 'great', 'happy', 'joy', 'fortunate']
    negative_words = ['bad', 'terrible', 'sad', 'unhappy', 'miserable']

    if any(word in text for word in positive_words):
        return "positive"
    elif any(word in text for word in negative_words):
        return "negative"
    else:
        return "neutral"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
