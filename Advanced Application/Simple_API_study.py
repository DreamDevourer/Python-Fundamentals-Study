"""
Simple API study inside Python.
Using Random Fox website to study API.
All HTTP response codes here: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

Basic sheet:

- Informational responses (100–199)
- Successful responses (200–299)
- Redirects (300–399)
- Client errors (400–499)
- Server errors (500–599)
"""

import requests
import json

# Getting the API url/path
responseAPI = requests.get('https://randomfox.ca/floof')

# print(responseAPI.status_code) # This will return a simple status code.
# print(responseAPI.text) # This will return a string value with the contents inside the API URL.
#
# Usually this will return a json.
# Output from the responseAPI.text => {"image":"https:\/\/randomfox.ca\/images\/25.jpg","link":"https:\/\/randomfox.ca\/?i=25"}
# Ok that's basicallly a json file, this is a web standard way to use API, so now we need to convert it to a python dictionary with json module.
#
# print(responseAPI.json())
#
# Awesome, now with the json() function, we have a dictionary.
# Output: {'image': 'https://randomfox.ca/images/13.jpg', 'link': 'https://randomfox.ca/?i=13'}
# Now let's play with variables and the API dictionary.
#
generatedFoxImg = responseAPI.json()

print("\nHere are all values from the API: \n")
# Let's pick each dictionary element individually and print it.
print(f"Your random fox: {generatedFoxImg['image']} \n")
print(f"Link to that fox: {generatedFoxImg['link']} \n")
