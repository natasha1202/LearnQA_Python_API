import requests

methods = {"method": ["POST", "GET", "PUT", "DELETE"]}

# part3. Correct pair method-request
for method in methods["method"]:
    if method == "GET":
        response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method[1])
        print(response.text)
    elif method == "POST":
        response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method[0])
        print(response.text)
    elif method == "PUT":
        response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method[2])
        print(response.text)
    elif method == "DELETE":
        response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method[3])
        print(response.text)