import requests

response = requests.get(url="http://appbrewery.github.io/news.ycombinator.com/")
print(response.text)

upload = soup.