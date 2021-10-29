"""
Fast API study inside Python.
All HTTP response codes here: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
To run this script: "uvicorn fast_api_study:appStudy --reload"
Always test things on the docs page: http://127.0.0.1:8000/docs

Basic response sheet:

- Informational responses (100–199)
- Successful responses (200–299)
- Redirects (300–399)
- Client errors (400–499)
- Server errors (500–599)

Requirements:

- Python 3.5+ (Used for this script: Python 3.9.2)
- fastapi (3.7.4)
- uvicorn (7.1.2)

Summary:

- ⚙️ Initial setup of fast API
- 🔖 GET method
- ✍️ POST method
- 🎭 PUT method
"""

# ============================== ⚙️ Initial setup of fast API ==============================
from fastapi import FastAPI, Path
from fastapi.params import Query
# It's recommended from the FastAPI documentation to import the following when using option parameters:
from typing import Optional
# Importing module for POST requests:
from pydantic import BaseModel
# Importing module for PUT requests:
from fastapi.encoders import jsonable_encoder

# This function is needed to start the API application.
appStudy = FastAPI()


# This class is for the POST request, you can come back here when you reach ✍️ POST method
class Item(BaseModel):
    name: str
    price: float
    # Optional parameter using Optional[] and None.
    quantity: Optional[int] = None


# This class is for the PUT request, you can come back here when you reach 🎭 PUT method
class updateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

# ============================== 🔖 GET method ==============================
#
# Now let's create an endpoint.
# An API endpoint is the point of entry in a communication channel when two systems are interacting.
# It refers to touchpoints of the communication between an API and a server.
# For example:
# /hello
# /hello/world
# These are endpoints from a server or URL. In this case we are using our machine, that means:
# http://localhost:8000/hello
#
# Now we need to create an endpoint method. These are all methods:
#
# GET, used to retrieve data from a server.
# POST, used to send data to a server, change values or create new data.
# PUT, used to update data on a server.
# DELETE, used to delete data on a server.
# PATCH, used to update data on a server without changing all the data.
# OPTIONS, used to retrieve information about the communication options available on a server.
# HEAD, used to retrieve only the headers of a response.
# CONNECT, used to connect to a remote server.
# TRACE, used to retrieve the entire request message as received by the server.
#
# Now we need to create a function that will be called when the endpoint is called.
# And call the method with ".get("PATH_HERE")" for example.
#


@appStudy.get("/")
def returnAPIValues():
    # Here we make a python dictionary that can be a json.
    # And now we need to open this script with "uvicorn fast_api_study:appStudy --reload" where the script file is located.
    # The syntax is simple: "uvicorn SCRIPT_NAME:FastAPI()-FUNCTION_VAR --reload"
    return {"DataStudy:": "Hello World!", "TestFieldTwo:": "test"}

# After running the script with uvicorn, test the documentation here: http://127.0.0.1:8000/docs


# Let's make more endpoints to test.
@appStudy.get("/about")
def returnAbout():
    return {"DataStudy:": "About"}


# Now let's play with some Inventory Management system, like a store does.
# This is actually the API values
inventoryDict = {
    "1": {"name": "Bread", "price": 1.25, "quantity": "10"},
    "2": {"name": "Milk", "price": 2.45, "quantity": "5"},
    "3": {"name": "Eggs", "price": 3.99, "quantity": "20"},
    "4": {"name": "Cheese", "price": 4.99, "quantity": "15"},
    "5": {"name": "Butter", "price": 5.00, "quantity": "5"}
}


# Now let's setup an endpoint. In this case, we are going to retrieve information from the inventory based on it's id.
@appStudy.get("/get-item/{individual_item_id}", response_model=updateItem)
# Ok, now we need to make a function with the individual item id with an INT type
# and add Path() parameter to add more details to a path parameter.
def getItem(individual_item_id: int = Path(None, description="The ID of the item you like to view")):
    return inventoryDict[str(individual_item_id)]


# Now we will need to work with query parameters.
# for example: facebook.com/home?redirect=Test&id=1
# Query parameters are basically syntaxed by "?" and "&"
@appStudy.get("/get-by-item-name")
# Observe that name: str don't have a Path() and it have a None value, which implies that this parameter name is optional.
# It's recommended from the FastAPI documentation to import optional module and use it in optional parameters.
def getItemName(name: Optional[str] = None):
    for invID in inventoryDict:
        if inventoryDict[invID]["name"] == name:
            return inventoryDict[invID]
    return inventoryDict["DataErr": "Item not found"]
# Ok let's test it here: http://127.0.0.1:8000/get-by-item-name?name=Bread
#  output: {"name":"Bread","price":1.25,"quantity":"10"}


# Great, now let's add a required parameter with the optional one and call it.
@appStudy.get("/test-multi-param")
# The idea here is to combine the name string parameter (optional) with a test int parameter.
# With the "*" basically we are saying that there is no limit for parameters in this call function without an order.
def getMultiItem(*, name: Optional[str] = None, test: int):
    for invID in inventoryDict:
        if inventoryDict[invID]["name"] == name:
            return inventoryDict[invID]
    return inventoryDict["DataErr": "Item not found"]
# Again, let's test it here: http://127.0.0.1:8000/test-multi-param?test=2&name=Milk
#  output: {"name":"Milk","price":2.45,"quantity":"5"}


# Let's combine path paramerters with query parameters together.
@appStudy.get("/get-by-item-name/{item_id}")
def getMultiItem(*, name: Optional[str] = None, item_id: int, test: int):
    for invID in inventoryDict:
        if inventoryDict[invID]["name"] == name:
            return inventoryDict[invID]
    return inventoryDict["DataErr": "Item not found"]
# Testing it here: http://127.0.0.1:8000/get-by-item-name/1/?test=2&name=Bread


# ============================== ✍️ POST method ==============================
# All good! Now let's study how POST method works.
@appStudy.post("/post-item/{item_id}")
def createItem(item_id: int, item: Item):
    # Let's create a new item id.
    if item_id in inventoryDict:
        return {"DataErr": "Item already exists"}
    else:
        inventoryDict[str(item_id)] = item
        return inventoryDict[str(item_id)]
# Testing here http://127.0.0.1:8000/docs#/default/getItem_get_item__individual_item_id__get
# by using the POST to add some eggs and then check if it worked using the check by id GET.
# Remeber that this method will be storing data on the RAM, this is not persistent, when the server reloads it will clear the POST data.


# ============================== 🎭 PUT method ==============================
# Time to study the PUT method!
@appStudy.put("/put-item/{item_id}")
def createItem(item_id: int, item: Item):
    # Let's create a new item id.
    if item_id in inventoryDict:
        return {"DataErr": "Item already exists"}
    else:
        inventoryDict[str(item_id)] = item
        return inventoryDict[str(item_id)]
# Testing here http://127.0.0.1:8000/docs#/default/getItem_get_item__individual_item_id__get


# ============================== 🎭 DELETE method ==============================
@appStudy.delete("/delete-item/{item_id}")
def createItem(item_id: int = Query(..., description="The ID of the item you like to delete")):
    # Let's create a new item id.
    if item_id in inventoryDict:
        return {"DataErr": "Item already exists"}
    else:
        del inventoryDict[str(item_id)]
        return {"Data DELETED": "Item deleted."}
