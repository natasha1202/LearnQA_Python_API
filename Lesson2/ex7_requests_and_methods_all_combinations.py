import requests

methods = {"method": ["POST", "GET", "PUT", "DELETE"]}

# part4. all possible pairs method-request

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params="GET")
print(response.text)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data="POST")
print(response.text)
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data="PUT")
print(response.text)
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data="DELETE")
print(response.text)

for method in methods:
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method)
        print(f'{method}, response text is {response.text}')
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
        print(f'{method}, response text is {response.text}')
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
        print(f'{method}, response text is {response.text}')
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method)
        print(f'{method}, response text is {response.text}')