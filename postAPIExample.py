import configparser
from payload import *
import requests
from utilities.configurations import *
from utilities.resources import *

posturl = getConfig()['API']['endpoint'] + ApiResources.addBook
headers={"Content-Type": "application/json"}
addBook_response = requests.post(posturl,json=addBookPayLoad("imftc"),headers= headers, )

print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']

# Delete Book
deleteurl = getConfig()['API']['endpoint'] + ApiResources.deleteBook
response_deleteBook = requests.post(deleteurl,
                                    json={
                                        "ID": bookId
                                    }, headers=headers, )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"


# Authentication
# Session Management
se = requests.session()
se.auth = auth=('SriramSameer', getPassword())

url = "https://api.github.com/user"
github_response = requests.get(url,verify=False,auth=('SriramSameer', getPassword()))

print(github_response.status_code)

url2 = "https://api.github.com/user/repos"
response = se.get(url2)
print(response.status_code)