import requests

response = requests.get("https://playground.learnqa.ru/api/homework_cookie")

print(response.cookies)
print(response.text)
print(response.headers)
print(response.cookies.get("HomeWork"))
