import requests

# Making a GET request
r = requests.get('https://api.github.com/users/naveenkrnl')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

#############
# Making a get request
response = requests.get('https://api.github.com/')

# print request object
print(response.url)

# print status code
print(response.status_code)

######
# import requests module
import requests

# Making a get request
response = requests.get('https://expired.badssl.com/', verify = False)

# print request object
print(response)

# providing
# Making a get request
response = requests.get('https://github.com', verify='/path/to/certfile')

# print request object
print(response)


#####

# import requests module
import requests

# create a session object
s = requests.Session()

# make a get request
s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')

# again make a get request
r = s.get('https://httpbin.org/cookies')

# check if cookie is still set
print(r.text)

