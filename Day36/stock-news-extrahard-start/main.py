import requests
from pyexpat.errors import messages
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "LFR5YW063MSBFA9G"
}
stocks = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"
stock_response = requests.get(stocks, params=stock_parameters)
stock_data = stock_response.json()['Time Series (Daily)']

data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference_in_price = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

diff_in_perc = round((difference_in_price / float(yesterday_closing_price)) * 100)

updown = None
if difference_in_price > 0:
    updown = "🔺"
else:
    updown = "🔻"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

if abs(diff_in_perc) > 5:
    news_parameters = {
        "apikey": "019f2f6191b14f66a7bacfbc5b8af42b",
        "qInTitle": COMPANY_NAME,
    }
    news_url = "https://newsapi.org/v2/everything?q=tesla"
    news_response = requests.get(news_url, params=news_parameters)
    news = news_response.json()['articles'][:3]
    print(news)
    formatted_news = [f"Headline: {new['title']}. in \Brief: {new['description']}" for new in news]
    TWILIO_SID = "PN0f4852def3449f8789f5dcc6cf0dea9d"
    TWILIO_AUTH_TOKEN = "f8db7c425aff7fbf59ab9088bd3a7fc2"

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_news:
        message = client.messages.create(
            body=article,
            from_="+14194629761",
            to="+918983356442"
        )



#Optional: Format the SMS message like this

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

