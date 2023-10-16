import requests

# part1. No parameters

def info_message(response):
    print(response.text)
    print(response.status_code)
    return

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
info_message(response1)
response2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
info_message(response2)
response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
info_message(response3)
response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
info_message(response4)



