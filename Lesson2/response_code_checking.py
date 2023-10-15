import requests
'''
response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.status_code)

response = requests.post("https://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/something")
print(response.status_code)
print(response.text)
'''
'''
response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response.status_code)
'''

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
second_response = response
print(first_response.url)
print(second_response.url)
# print(response.status_code)