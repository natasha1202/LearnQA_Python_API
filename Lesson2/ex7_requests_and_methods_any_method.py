import requests

# part2. HEAD-request
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
print(response.status_code)