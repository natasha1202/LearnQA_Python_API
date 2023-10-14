import requests

response = requests.get("https://playground.learnqa.ru/api/check_type")
print(response.text)
response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.text)
response = requests.delete("https://playground.learnqa.ru/api/check_type")
print(response.text)
response = requests.put("https://playground.learnqa.ru/api/check_type")
print(response.text)

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
print(response.text)