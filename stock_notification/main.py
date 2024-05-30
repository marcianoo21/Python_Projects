import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "K7DX0H4LAI2VDEDM"
NEWS_API_KEY = "07c9513bf3044225bb760ce16f7f98fb"
TWILIO_SID = "TWILIO_SID"
AUTH_TOKEN = "AUTH_TOKEN"

    

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)

data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
#print(yesterday_closing_price)
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]
#print(day_before_yesterday_closing_price)
absolute_difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if absolute_difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
#print(up_down)
diff_percent = round(absolute_difference / float(yesterday_closing_price) * 100)
#print(diff_percent)
if abs(diff_percent) >= 1:

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME, 
    }


    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    
    three_articles = articles[:3]
    #print(three_articles)


    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]


    client = Client(TWILIO_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            from_='phone_number',
            body=article,
            to='phone_number'
        )

