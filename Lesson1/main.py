import requests

# print('Hello, world!')

print('Hello from Natalia')

# response = requests.get("https://playground.learnqa.ru/api/hello")
# print(response.text)

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)