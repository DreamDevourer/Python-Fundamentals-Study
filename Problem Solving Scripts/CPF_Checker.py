#!/usr/bin/env python3

"""
Algorithm for validating CPF
The CPF calculation is based on the final 2 digits.
To validate, take the first 9 digits of the CPF, generate the 2 digits and save in a new CPF.
Compare if the CPF sent is the same as the CPF generated.
If true, the CPF is valid, otherwise invalid.

* Get first digit:
--- Multiply the first 9 digits of the CPF by a count regress starting from 10 and ending at 2.
--- Add all the multiplication values from step 1
--- Get the remainder of the division between the sum and 11 from step 2
--- Subtract the result from step 3 by 11
--- If the result of step 4 is greater than nine, the digit is zero, otherwise the digit is the value from step 4

* Get second digit:
--- Multiply the first 9 digits of the CPF, PLUS THE FIRST DIGIT, previously obtained by a countdown starting from 11 and ending in 2
--- Same logic as step 2 from the first digit onwards.

SAMPLE CPF: 113.314.390-35

1*10 = 10
1*9 = 9
3*8 = 24
3*7 = 21
1*6 = 6
4*5 = 20
3*4 = 12
9*3 = 27
0*2 = 0

DIGITS SUM: 1 + 1 + 3 + 3 + 1 + 4 + 3 + 9 + 0 + 3 + 5 = 33
TOTAL: 10 + 9 + 24 + 21 + 6 + 20 + 12 + 27 + 0 + 0 = 129

"""

import re

debugMode = True


def logThis(message):
    if debugMode:
        print(message)


class CPF_Validator_N:
    def __init__(self, userCPF):
        self.userCPF = userCPF

    @property
    def validateCPF(self):
        return self.userCPF

    # if debugMode:
    #     sampleCPF = "113.314.390-35"
    #     print(f"Sample CPF for testing: {sampleCPF}")
    #     userCPF = input("CPF: ")
    validCPF = None

    @staticmethod
    # Validates a CPF number with the easy way.
    def validateCPF(userCPF):
        # regular expression to remove any non-numeric characters, spaces, dots or dashes.
        userCPF = re.sub("[^0-9]", "", userCPF)
        logThis(userCPF)

        # Check length of CPF
        if len(userCPF) != 11:
            validCPF = False
            logThis("CPF is NOT valid.")
            return validCPF
        else:

            # Separate all numbers from userCPF into a list.
            userCPFList = list(userCPF)
            # Sum every integer of the userCPFList
            sumOfDigits = sum(int(i) for i in userCPFList)
            sumOfDigits = str(sumOfDigits)

            if sumOfDigits[0] == sumOfDigits[1]:
                logThis("CPF partially valid.")

            #  Get first nine digits from userCPF
            firstNineDigits = userCPFList[0:9]
            sumMaster = 0
            for key, multiply in enumerate(range(len(firstNineDigits) + 1, 1, -1)):
                # logThis(f"{userCPFList[key]} * {multiply}")
                sumMaster += int(userCPFList[key]) * multiply
            restSum = 11 - (sumMaster % 11)

            if restSum > 9:
                restSum = 0

            logThis(f"Rest sum: {restSum}")
            mergeRes = str(userCPF[:9]) + str(restSum)
            logThis(f"Merged result: {mergeRes}")


if __name__ == "__main__":
    sampleCPF = "113.314.390-35"
    CPF_Validator_N.validateCPF(sampleCPF)
