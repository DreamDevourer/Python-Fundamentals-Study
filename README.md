<h1 align="center">Python Fundamentals Study 📚</h1>

<p align="center">This repository is dedicated for my fundamental knowledge related to Python 3 and newer. I intend to work on this repository weekly.</p>

<p align="center">
  <a href="https://github.com/DreamDevourer/Python-Fundamentals-Study/blob/main/LICENSE">License</a>
</p>

<img src="./sample.svg" alt="Sample password generator script study." width="100%" height="auto">

<p>In this repository I study the practical application of:</p>
<ul>
  <li>Python built-in functions</li>
  <li>Types of numeric data (such as int and float)</li>
  <li>Strings Formatting</li>
  <li>Variables</li>
  <li>Mathematical operations with Python</li>
  <li>Libraries</li>
  <li>Decision making (if, elif, else)</li>
  <li>Repetitions (while, for)</li>
  <li>User-defined functions (def())</li>
  <li>My knowledge of English and general Python use.</li>
  <li>Advanced use cases</li>
</ul>

## 🗺 Directory Map

<ol>
<li><a href="#advanced">Advanced Applications</a></li>
<li><a href="#conversion">Conversion Scripts</a></li>
<li><a href="#math">Math Scripts</a></li>
<li><a href="#problemSolving">Problem Solving Scripts</a></li>
<li><a href="#string">String Based Scripts</a></li>
</ol>

<br>

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| **Advanced Application** | **Conversion Scripts** | **Math Scripts** | **Problem Solving Scripts** | **String Based Scripts** |
| Password Generator | Ordinal numbers to Roman numbers | Circle Area Calculation | Simple Investment Income Calculator | Basic Input exercise |     |
| Get Phone Number Details | Time Conversion | Fibonacci Sequence | Bonus percentage and salary calculation | Copy strings to clipboard |     |
| Web Stock Tracking App | Minutes to Years | Rectangle Area Calculation | Quantity per size calculation | Hide string inside JPG files |     |
| Website Link Picker | Temperature Conversion | Trapeze Area Calculation | Price by quantity calculation | Reverse String |     |
|     | Images to WebP |     | Q-min jump arrays |     |     |
|     | Image metada optimization |     |     |     |     |

<br>

<h4 id="advanced">1. Advanced Applications</h4>
<p>Advanced scripts related to daily and possible market problems solving, high use of all practical applications on each script.</p>

<h4 id="conversion">2. Conversion Scripts</h4>
<p>Scripts with focus on conversion operations, using part of practical application topics</p>

<h4 id="math">3. Math Scripts</h4>
<p>Mathematical operations scripts to calculate and/or give mathematical results.</p>

<h4 id="problemSolving">4. Problem Solving Scripts</h4>
<p>These scripts are daily general problem solving scripts, like an investment calculator, a salary bonus calculation, price per quantity, etc.</p>

<h4 id="string">5. String Based Scripts</h4>
<p>Simple and direct strings scripts with minimal interaction with the user.</p>

## 💡 Useful Snippets and study pieces

<p>Here are some useful snippets to use daily for boosting code efficiency. Every single snippet is coming from a study script that I made from this repository.</p>

<h3>Dynamic File Path</h3>
<p>Useful for loading external assets in specific directories and subdirectories, this snippet will work on every major OS like Windows, MacOS, Linux and BSD.</p>

```python
import pathlib
from pathlib import Path

# Dynamic File Path Solution
OUTPUT_PATH = pathlib.Path(__file__).parent.absolute()
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
```

<h3>While</h3>
<p>While can be used to start a script on the core part of it or to use as a logic operator.</p>

```python
while True:
    answer = input("Do you want to try again? (Y/n) ")
    if answer == 'y' or answer == 'Y' or sys.stdin.isatty():
        num = int(input("Enter a number: "))
        print(num2roman(num))
    elif answer == 'n':
        break
    else:
        print("Invalid input.")
```

<h3>For loops</h3>
<p>For loops are essential these days, there is no doubt about that. It's possible to make a huge range of logical solutions with lists, arrays and other variables.</p>

```python
for link in linksFinder:
    print(link.get("href"))

    saveFile = input(
        "Do you want to save this list inside a text file? (y/n) ")
    if saveFile == "y":
        with open("links.txt", "a") as file:
            file.write(link.get("href") + "\n")
    else:
        pass
```

<h3>Bytes Encode and Decode</h3>
<p>Bytes converts an object to an immutable byte-represented object of given size and data, which is useful for writing or reading HEX values inside a file.</p>

```python
    # Bytes Encode and Decode Study

    def writeString():
        # Write a string at the end of a JPG file.
        with open(relative_to_assets('photo.jpg'), 'ab') as f:  # ab append bytes mode
            f.write(b' Hidden message: test :)') # b is for bytes

    def readString():
        # Read HEX of the JPG file.
        with open(relative_to_assets('photo.jpg'), 'rb') as f:  # Read bytes mode
            jpgContent = f.read()
            # when FF D9 occurs.
            offset = jpgContent.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            print(f.read())

    def deleteString():
        # delete everything after the last FF D9 from a JPG file
        with open(relative_to_assets('photo.jpg'), 'r+') as f:  # Read bytes mode
            jpgContent = f.read()
            offset = jpgContent.index(bytes.fromhex('FFD9'))
            f.seek(offset + 2)
            f.truncate()
```

<h3>Endswith</h3>
<p>This function returns True if a string ends with the specified suffix (case-sensitive), otherwise returns False. A tuple of string elements can also be passed to check for multiple options. For startswith we have a similar approach.</p>

```python
from pathlib import Path
import pathlib
files = os.listdir(ASSETS_PATH)

# Interesting solution to pick specific files inside a list.
for file in files:
    if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
      print(f"Optimizing {file}")
      imgOptimize = Image.open(relative_to_assets(str(file)))
      imgWidth, imgHeight = imgOptimize.size
    else:
      print(f"{file} is not a PNG or JPG, skipping")
```

<h3>Regular Expression</h3>
<p>Regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world.</p>

```python
import re
    
# Regular Expression from module re;
# https://docs.python.org/3/library/re.html
# validate def will make sure that the remTwo var can have a "." as float


def validate(string):
    result = re.match(r"(\+|\-)?\d+(\.\d+)?$", string)
    return result is not None
```

<h3>Using Shell Paths</h3>
<p>Usually when we need to call a shell script within a python script, paths tends to break and not be cross compatible between python and shell lines. So this snippet helps to solve that.</p>

```python
import os
import sys

# Python path. This will pick the current directory where the script is located.
current_dir = os.path.dirname(sys.argv[0])

# Shell path. This will pick "current_dir" and replace any possible empty spaces with "\" and other fixes to be compatible with any unix-like Shell.

fixDirPath = current_dir.replace(" ", "\\ ").replace("?", "\\?").replace("&", "\\&").replace(
    "(", "\\(").replace(")", "\\)").replace("*", "\\*").replace("<", "\\<").replace(">", "\\>")


targetDirectory = "Sample"

# Sample script usage to delete a directory using shell commands
os.system(f"rm -rf {str(fixDirPath)}/{str(targetDirectory)}")
```

<h3>Input</h3>
<p>Input is a built-in function in Python, allows coders to receive information through the keyboard, which they can process in a Python program. This is basic and essential.</p>

```python
# Simple like that :)
userString = input("Enter a text: ")
print(userString[::-1]) # Reverse the string
```

<h3>Time Conversion</h3>
<p>Making mathematical operations inside python are easy things to do, you basically need to know the formula and the logic to implement conversion and precision operations.</p>

```python
minutes = "24.785089"
print(minutes + " minutes is equal to " +
      str(float(minutes)/60/24/365) + " years.")
```

<h3>Ordinal Numbers to Roman Numbers</h3>
<p>With a simple array, it's possible to compare ordinal numbers with strings that represents roman numbers.</p>

```python
num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

# Function to convert the numbers to roman values. Based on NullDev algorithm.


def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman
```

<h3>Temperature Conversion</h3>
<p>Converting temperature units is a simple task, all that is needed is the formula of each unit.</p>

```python
# Simple formulas to convert temperature from Celsius to Fahrenheit and vice versa.
fahrenheit = celsius * 9 / 5 + 32
celsius = (fahrenheit - 32) * 5 / 9
```

<h3>Copy to Clipboard</h3>
<p>When copying content to the user's clipboard, it's needed to import the OS module to use features like that.</p>

```python
import os
nameGen = "Hello there :)"
# Copy to the variable "nameGen" to the clipboard
os.system(f"echo {nameGen} | pbcopy")
```

<h3>Open Website or Application</h3>
<p>Opening external websites or applications also requires the OS module to be imported, this snippet allows the script to open almost every type of file, like Shell scripts, default applications and websites.</p>

```python
import os
targetSite = "https://google.com/"
os.system(f"open {targetSite}")
```


<h3>Watchdog Usage</h3>
<p>Watchdog is used to monitor events on the OS, that means that it's possible to monitor files and folders. To be more specific: Python API library and shell utilities to monitor file system events.</p>

```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

currentUser = "default"
mainDirectory = f"/Users/{currentUser}/Downloads"
jobDestinationPath = f"/Users/{currentUser}/Documents/Remotish"

class MyHandler(FileSystemEventHandler): # We need to create a class with the FileSystemEventHandler

    # After that we need to make a function with self and event. So when anything happens to the folder it will execute the function.
    def on_modified(self, event):
        for individualFile in os.listdir(mainDirectory):
            os.rename(f"{mainDirectory}/{individualFile}", f"{jobDestinationPath}/{individualFile}")

# Needed to monitor Watchdog
eventHandler = MyHandler()
observer = Observer()
observer.schedule(eventHandler, mainDirectory, recursive=True)
observer.start()

# Needed to monitor Watchdog
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```


<h3>Simple JSON read method</h3>
<p>JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. These days, JSON is mandatory. This little snippet can read a json file and output its content.</p>

```json
// SAMPLE JSON FILE
{
    "username": "testABC",
    "password": "testDEF"
}
```

```python
import json
import sys
import os

userContent = {}
current_dir = os.path.dirname(sys.argv[0])

with open(f"{current_dir}/sample-json.json", "r") as json_file:
    userContent = json.load(json_file)
    print(userContent["username"])
    print(userContent["password"])
```

<h3>Simple JSON write method</h3>
<p>This little snippet can write a json file and output its content.</p>

```json
// SAMPLE JSON FILE
{
    "username": "testABC",
    "password": "testDEF"
}
```

```python
import json
import sys
import os

userContent = {}
current_dir = os.path.dirname(sys.argv[0])

userInp = input("Enter your username: ")
userInp2 = input("Enter your password: ")

userContent["username"] = f"{str(userInp)}"
userContent["password"] = f"{str(userInp2)}"


with open(f"{current_dir}/sample-json.json", "w") as json_file:
    json.dump(userContent, json_file)
    print("The new username is: " + str(userContent["username"]))
    print("The new password is: " + str(userContent["password"]))
```


<h3>Simple API Read Methods</h3>
<p>Here are some ways to read the API path content with a simple GET method and some extra calls.</p>

```python
import requests
import json

responseAPI = requests.get('https://randomfox.ca/floof')

# This will return a simple status code.
print(responseAPI.status_code)
# This will return a string value with the contents inside the API URL.
print(responseAPI.text)
# Now printing json format and using as a dictionary.
print(responseAPI.json())
```


<h3>Simple API GET Method</h3>
<p>Reading values from an API can be done very easily by using the requests module and also to converting the API values into Python dictionaries using json module and function.</p>

```python
import requests
import json

# Getting the API url/path
responseAPI = requests.get('https://randomfox.ca/floof')
# Output from GET: {'image': 'https://randomfox.ca/images/13.jpg', 'link': 'https://randomfox.ca/?i=13'}
generatedFoxImg = responseAPI.json()

print(f"Your random fox: {generatedFoxImg['image']} \n")
```


<h3>FastAPI GET Method</h3>
<p>FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. Making GET requests are easy thing to do, just need to import the module and associate the function to a variable and start coding paths and parameters with the FastAPI Functions.</p>

```python
from fastapi import FastAPI

appStudy = FastAPI()


@appStudy.get("/")
async def root():
    return {"messageField": "Message content here."}
```

<h3>FastAPI POST Method</h3>
<p>The POST method is used to request that the origin server accept the entity attached in the request as a new subordinate of the resource identified by the Request-URI in the Request-Line.</p>

```python
from fastapi import FastAPI, Path
from pydantic import BaseModel

appStudy = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: Optional[int] = None

# This is actually the API values
inventoryDict = {
    "1": {"name": "Bread", "price": 1.25, "quantity": "10"},
    "2": {"name": "Milk", "price": 2.45, "quantity": "5"},
    "3": {"name": "Eggs", "price": 3.99, "quantity": "20"},
    "4": {"name": "Cheese", "price": 4.99, "quantity": "15"},
    "5": {"name": "Butter", "price": 5.00, "quantity": "5"}
}

# Using POST method
@appStudy.post("/post-item/{item_id}")
def createItem(item_id: int, item: Item):
    # Let's create a new item id.
    if item_id in inventoryDict:
        return {"DataErr": "Item already exists"}
    else:
        inventoryDict[str(item_id)] = item
        return inventoryDict[str(item_id)]
```


<h3>FastAPI PUT Method</h3>
<p>PUT method requests for the attached entity (in the request body) to be stored into the server which hosts the supplied Request-URI. If the Request-URI refers to an already existing resource – an update operation will happen</p>

```python
from fastapi import FastAPI, Path
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from typing import Optional

appStudy = FastAPI()

# This class is for the PUT request
class updateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[int] = None

# This is actually the API values
inventoryDict = {
    "1": {"name": "Bread", "price": 1.25, "quantity": "10"},
    "2": {"name": "Milk", "price": 2.45, "quantity": "5"},
    "3": {"name": "Eggs", "price": 3.99, "quantity": "20"},
    "4": {"name": "Cheese", "price": 4.99, "quantity": "15"},
    "5": {"name": "Butter", "price": 5.00, "quantity": "5"}
}

# PUT method
@appStudy.put("/put-item/{item_id}")
def createItem(item_id: int, item: Item):
    # Let's create a new item id.
    if item_id in inventoryDict:
        return {"DataErr": "Item already exists"}
    else:
        inventoryDict[str(item_id)] = item
        return inventoryDict[str(item_id)]
```

## 📄 License

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

| Permissions | Restrictions | Conditions
| --- | --- | --- 
&check; Commercial Use | &times; Liability | &#x1f6c8; License and Copyright Notice
&check; Modification   | &times; Warranty | &#x1f6c8; State changes
&check; Distribution |  | &#x1f6c8; Disclose source
&check; Patent Use |  | &#x1f6c8; Same license
&check; Private Use
