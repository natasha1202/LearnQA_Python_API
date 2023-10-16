import requests

method_list = ["POST", "GET", "PUT", "DELETE"]
payload = {"method": method_list}

# part3. Correct pair method-request
for method in method_list:
    if method == "GET":
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
        print(response.text)
        print(response.status_code)
    elif method == "POST":
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        print(response.text)
        print(response.status_code)
    elif method == "PUT":
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        print(response.text)
        print(response.status_code)
    elif method == "DELETE":
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
        print(response.text)
        print(response.status_code)