import json

import requests
import time
import random

# response1 creates a job
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

response_text = response1.text
json_obj = json.loads(response_text)
token = json_obj["token"]
print(response_text)

# response2 gets existing token from response1 as parameter
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=token)
print(response2.text)

# response3 and response4 get token and time as parameters
waiting_time = {"seconds": json_obj["seconds"]}
random_time1 = random.randint(0, int(waiting_time["seconds"]))
random_time2 = random.randint(int(waiting_time["seconds"]), int(waiting_time["seconds"])+10)

#  Job is NOT ready
time.sleep(random_time1)
playload = {"token": token, "seconds": random_time1}
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=playload, )
print(response3.text)

# Job is ready
time.sleep(random_time2)
playload = {"token": token, "seconds": random_time2}
response4 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=playload, )
print(response4.text)


# request with not existing token
not_existing_token = {"token": "abcd"}
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=not_existing_token)
print(response3.text)
