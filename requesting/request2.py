import requests
from requests.auth import HTTPBasicAuth

# Making a get request
response = requests.get('https://api.github.com/blad00,',
                        auth=HTTPBasicAuth('bladoxp@gmail.com', 'S!stema12sun'))

# print request object
print(response)
