import requests
from utilities.resources import *
from utilities.configurations import *

def after_scenario(context, scenario):
    if "library" in scenario.tags:
        deleteurl = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        response_deleteBook = requests.post(deleteurl,
                                        json={
                                            "ID": context.bookId
                                        }, headers={"Content-Type" : "application/json"}, )

        assert response_deleteBook.status_code == 200
        res_json = response_deleteBook.json()

        print(res_json["msg"])
        assert res_json["msg"] == "book is successfully deleted"
