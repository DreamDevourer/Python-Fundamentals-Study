import requests
from bs4 import BeautifulSoup


print("Welcome to Website Link Extractor.")
targetURL = input("Add here the target website to extract links: ")

requestFromURL = requests.get(targetURL).content
soupModule = BeautifulSoup(requestFromURL, "html.parser")
linksFinder = soupModule.find_all("a")

for link in linksFinder:
    print(link.get("href"))

    saveFile = input(
        "Do you want to save this list inside a text file? (y/n) ")
    if saveFile == "y":
        with open("links.txt", "a") as file:
            file.write(link.get("href") + "\n")
    else:
        pass
