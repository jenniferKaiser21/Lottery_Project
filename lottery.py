from random import choices
import sys
sys.path.append('api.py')
from api import api_token

"""
API connection code provided by:
https://collectapi.com/api/chancegame/lottery-api
"""
# import http.client

# conn = http.client.HTTPSConnection("api.collectapi.com")

# headers = {
#     'content-type': "application/json",
#     'authorization': api_token
# }

# conn.request("GET", "/chancegame/usaPowerball", headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))
