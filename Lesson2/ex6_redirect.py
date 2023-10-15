import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

count = len(response.history)
last_response = response.history[count-1]
print(last_response.url)

