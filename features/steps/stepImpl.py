import requests
from behave import *
from payload import *
from utilities.resources import *
from utilities.configurations import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayLoad("manjkk", "444")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers, )

@then(u'the book is successfully installed')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json["Msg"] == "successfully added"


@given('the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayLoad(isbn,aisle)



@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('SriramSameer', getPassword())


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then('status code of response should be {statusCode:d}')
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode