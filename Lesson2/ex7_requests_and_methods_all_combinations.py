import requests

method_list = {"POST", "GET", "PUT", "DELETE"}


def info_message(response):
    print(response.status_code)
    print(response.text)


# part4. all possible pairs method-request

for method in method_list:
    payload = {"method": method}
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
    print(f'GET-request, method = {method}')
    info_message(response)
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f'POST-request, method = {method}')
    info_message(response)
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f'PUT-request, method = {method}')
    info_message(response)
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
    print(f'DELETE-request, method = {method}')
    info_message(response)
