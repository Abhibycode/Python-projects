import datetime

import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "fdlakhfjkladsds"
USERNAME = "kabhis"

user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "tracker",
    "name": "Task Tracker",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response_graph = requests.post(url=graph_endpoint, json=graph_config, headers= headers)
# print(response_graph.text)

today = datetime.datetime.now()
print(today.strftime("%Y%m%d"))

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_config['id']}/"
pixel_config = {
    "date": str(today.strftime("%Y%m%d")),
    "quantity": "7"
}

# response_pixel = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response_pixel.text)
pixel_update = f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_config['id']}/{today.strftime("%Y%m%d")}"
response_pixel = requests.put(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response_pixel.text)