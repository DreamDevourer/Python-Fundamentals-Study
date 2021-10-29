""" Made by Nicolas Mendes - Sept 24 2021
Script to study how to use time and clipboard.
"""
from datetime import date, timedelta
import os

namePrint = "Name Last Name"
# Pick current month
currentMonth = date.today().month
# Pick current day
currentDay = date.today().day
# Randomly change between 1 and 9 mins.
randomMins = int(os.urandom(1).hex(), 16) % 9 + 1
hourGen = f"14:0{str(randomMins)}"
targetSite = "https://discord.com/channels/XXXXX/XXXXX"
print(f"The random time is: {hourGen}")


def allFriday(year):
    d = date(year, 1, 1)                    # Jan 1
    d += timedelta(days=4 - d.weekday())  # First Friday
    while d.year == year:
        yield d
        d += timedelta(days=7)


for dia in allFriday(2021):
    if dia.day == currentDay and dia.month == currentMonth:
        nameGen = f"{currentDay}/{currentMonth} - {namePrint}"
        print(nameGen)
        # Copy to the variable "nameGen" to the clipboard
        os.system(f"echo {nameGen} | pbcopy")
        os.system(f"open {targetSite}")
