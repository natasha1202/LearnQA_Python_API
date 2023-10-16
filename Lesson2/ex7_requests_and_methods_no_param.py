import requests

# part1. No parameters
response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response1.text)
print(response1.status_code)
response2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response2.text)
print(response2.status_code)
response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response3.text)
print(response3.status_code)
response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response4.text)
print(response4.status_code)


