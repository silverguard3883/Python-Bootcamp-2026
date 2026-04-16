import requests
from datetime import datetime

"""
GET requests data from an external system
Example: requests.get()

POST writes data to an external system
Example: requests.post()

PUT updates data to an external system
Example: requests.put()

DELETE deletes data from an external system
Example: requests.delete()

"""
USERNAME = "silverguard"
PIXELA_TOKEN = "thisisasecret"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_PARAMETERS = {
    "token":"thisissecret",
    "username":"silverguard",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

create_pixela_user = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_PARAMETERS)

pixela_graph = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXELA_GRAPH_PARAMETERS = {
    "id": "graph1",
    "name": "Studying",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

#create_pixela_graph = requests.post(url=pixela_graph, json=PIXELA_GRAPH_PARAMETERS, headers=headers)
#print(create_pixela_graph.text)
current_date = datetime.now().strftime("%Y-%m-%d")

PIXEL_PARAMETERS = {
    "date": current_date,
    "quantity": "1"
}

create_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
requests.post(url=create_pixel_endpoint, json=PIXEL_PARAMETERS, headers=headers)




