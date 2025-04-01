from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

# Function to analyze sentiment
def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity  # Sentiment score (-1 to 1)
    
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form["user_input"]
        sentiment = analyze_sentiment(user_text)

    return render_template("index.html", sentiment=sentiment, user_text=user_text)

if __name__ == "__main__":
    app.run(debug=True)

