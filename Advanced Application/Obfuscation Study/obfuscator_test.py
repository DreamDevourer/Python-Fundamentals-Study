# This is just a test script that I will be obfuscating with pyarmor.
testString = "Hi, welcome to this simple piece of software!"
testBool = None
testInt = 10

testInput = input("Please enter a string: ")

if testInput != "":
    print(f"You entered: {testInput}")
    print(testBool)
    print(testInt)
else:
    testBool = True
    testInt = 20
    print(testBool)
    print(testInt)
    print(f"Empty String!!")
