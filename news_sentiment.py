import requests
import os
import nltk
from flask import Flask, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
from newsapi import NewsApiClient
from dotenv import load_dotenv

nltk.download('vader_lexicon')

load_dotenv()

app = Flask(__name__)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

sia = SentimentIntensityAnalyzer()

@app.route('/', methods=['GET'])
def main():
    return jsonify({'message': 'News API server is working'})

@app.route("/sentiment_analysis", methods=['GET'])
def sentiment_analysis():
    try:
        response = newsapi.get_everything(
            q="crude oil",
            language="en",
            sort_by="relevancy",
            page_size=20  # Limit to 20 articles
        )

        articles = response['articles']

        #filtered_articles = [article for article in articles if article['source']['name'] != 'Yahoo Entertainment']

        sentiments = []

        for article in articles:
            title = article['title']
            source_name = article['source']['name']
            description = article['description']
            content = article.get('content', '')

            text = f"{title}. {description}. {content}"

            sentiment_score = sia.polarity_scores(text)

            sentiments.append({
                "title": title,
                "source": source_name,
                "description": description,
                "content": content,
                "sentiment": sentiment_score
            })

        return jsonify({
            "status": "success",
            "articles": sentiments
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
