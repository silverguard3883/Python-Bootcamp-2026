import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_ENDPOINT_API_KEY = "EKEVBCFK6VBBHSBM"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_ENDPOINT_API_KEY,
}

stock_request = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMETERS)
stock_request.raise_for_status()
stock_data = stock_request.json()

#print(stock_data)

NEWS_ENDPOINT = "https://newsdata.io/api/1/latest"
NEWS_ENDPOINT_API_KEY = "pub_0d1b1b7667e241988c51a12c3c6b9b88"
queries = [
    "Tesla stock TSLA",
    "Tesla earnings report",
    "Tesla Inc financial results",
    "Elon Musk Tesla news",
]

NEWS_PARAMETERS = {
    "apikey": NEWS_ENDPOINT_API_KEY,
    "q": queries[0],
    "language": "en",
}

time_series = stock_data["Time Series (Daily)"]

# Get list of dates (already in descending order with newest first)
dates = list(time_series.keys())

yesterday_close = float(time_series[dates[1]]["4. close"])
day_before_yesterday_close = float(time_series[dates[2]]["4. close"])

print("Yesterday:", yesterday_close)
print("Day before yesterday:", day_before_yesterday_close)

percentage_difference = abs(yesterday_close - day_before_yesterday_close) / day_before_yesterday_close * 100
print("Percent difference:", percentage_difference)

if percentage_difference > 5:
    news = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMETERS, timeout=10)
    news.raise_for_status()
    news_data = news.json()

    articles = news_data.get("results", [])[:3]

    symbol = "🔺" if percentage_difference > 0 else "🔻"

    formatted_articles = [
        f"{STOCK_NAME}: {symbol}{percentage_difference:.2f}%\n"
        f"Headline: {article.get('title', 'No title')}\n"
        f"Brief: {(article.get('description') or 'No description')[:150]}\n"
        f"Link: {article.get('link', 'No link')}"
        for article in articles
    ]

    for item in formatted_articles:
        print(item)
        print("-" * 40)

    account_sid = os.environ["TWILIO_ACCOUNT_SID"]
    auth_token = os.environ["TWILIO_AUTH_TOKEN"]
    twilio_number = os.environ["TWILIO_PHONE_NUMBER"]
    my_number = os.environ["MY_PHONE_NUMBER"]

    client = Client(account_sid, auth_token)

    for article_text in formatted_articles:
        message = client.messages.create(
            body=article_text,
            from_=twilio_number,
            to=my_number,
        )
        print(message.sid)