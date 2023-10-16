import requests

method_list = {"POST", "GET", "PUT", "DELETE"}


def info_message(response):
    print(method)
    print(response.text)
    print(response.status_code)


# part3. Correct pair method-request
for method in method_list:
    payload = {"method": method}
    if method == "GET":
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
        info_message(response)
    elif method == "POST":
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        info_message(response)
    elif method == "PUT":
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        info_message(response)
    elif method == "DELETE":
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        info_message(response)
