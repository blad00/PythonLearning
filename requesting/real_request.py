import requests

response = requests.get('https://api.github.com')

# Status
print(response.status_code)

if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')

if response:
    print('Success!')
else:
    print('An error has occurred.')

import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

# content
response = requests.get('https://api.github.com')
print(response.content)
print(response.text)

response.encoding = 'utf-8' # Optional: requests infers this internally
print(response.text)

response.json()

# Headers
response.headers

response.headers['Content-Type']

# Query String Parameters
import requests

# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspect some attributes of the `requests` repository
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

# before we pass as list, now will pass as dictionary
requests.get(
    'https://api.github.com/search/repositories',
    params=[('q', 'requests+language:python')],
)

# bytes
requests.get(
    'https://api.github.com/search/repositories',
    params=b'q=requests+language:python',
)

# Request Headers

import requests

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

# Other HTTP Methods
requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
response = requests.delete('https://httpbin.org/delete')
json_response = response.json()
print(json_response['args'])

requests.head('https://httpbin.org/get')
response = requests.head('https://httpbin.org/get')
response.headers['Content-Type']

requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')

# The Message Body
# dict
requests.post('https://httpbin.org/post', data={'key':'value'})
# List of tuples
requests.post('https://httpbin.org/post', data=[('key', 'value')])

response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
json_response['data']

json_response['headers']['Content-Type']

# Inspecting Your Request

response = requests.post('https://httpbin.org/post', json={'key':'value'})
response.request.headers['Content-Type']

response.request.url

response.request.body

# Authentication
from getpass import getpass
requests.get('https://api.github.com/user', auth=('blad00', getpass()))

from requests.auth import HTTPBasicAuth
from getpass import getpass
requests.get(
    'https://api.github.com/user',
    auth=HTTPBasicAuth('username', getpass())
)

