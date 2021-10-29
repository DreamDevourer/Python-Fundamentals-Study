"""
Documentation
https://pypi.org/project/phonenumbers/
"""
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

print("Welcome to Phone Number Details.")
print("Sample number: +442083661177")
deviceNumber = input("Enter the phone number: ")
deviceNumber = phonenumbers.parse(str(deviceNumber))
print(deviceNumber)

# get timezone from phone number and print it
timezone_result = timezone.time_zones_for_number(deviceNumber)
print("Timezone: ", timezone_result[0])

# get carrier from device number and print it
carrier_result = carrier.name_for_number(deviceNumber, None)
print("Carrier: ", carrier_result)

# get location from device number and print it
location_result = geocoder.description_for_number(deviceNumber, None)
print("Location: ", location_result)

# validate device number and print it
print("Is valid: ", phonenumbers.is_valid_number(deviceNumber))

# check possibility of a number.
print("Possible: ", phonenumbers.is_possible_number(deviceNumber))
