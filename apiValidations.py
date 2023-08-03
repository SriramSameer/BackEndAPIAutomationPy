import json
from utilities.resources import *
from utilities.configurations import *
import requests

geturl = getConfig()['API']['endpoint'] + ApiResources.getBookAuthor
response = requests.get(geturl,
             params={'AuthorName':'Mark Lutz'},)
# print(response.text)
# print(type(response.text))
# dict_response = json.loads(response.text)
# print(dict_response[0]['isbn'])

# Easier method
json_response = response.json()
print(type(json_response))
print(json_response[0]['isbn'])
# print(response.status_code)
assert response.status_code == 200
print(response.headers)
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
# Retrieve the book details with ISBN
for actualBook in json_response:
    print(type(actualBook))
    if actualBook['isbn'] == 'klo':
        print(actualBook)
        break

expectedBook = {
        "name":"Learn Appium Automation with Python",
        "isbn":"klo",
        "aisle":"777",
        "author":"Mark Lutz"
}

assert actualBook == expectedBook
