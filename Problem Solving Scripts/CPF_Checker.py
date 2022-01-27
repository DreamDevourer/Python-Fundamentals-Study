#!/usr/bin/env python3

""" Nicolas Mendes - Jan 18 2022

Based on https://www.alura.com.br/conteudo/python-validacao-dados#:~:text=Criando%20um%20novo%20Python%20file,contr%C3%A1rio%20o%20retorno%20ser%C3%A1%20False%20

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

TO GET FIRST DIGIT FORM LAST SECTION:

1*10 = 10
1*9 = 9
3*8 = 24
3*7 = 21
1*6 = 6
4*5 = 20
3*4 = 12
9*3 = 27
0*2 = 0

TOTAL: 10 + 9 + 24 + 21 + 6 + 20 + 12 + 27 + 0 + 0 = 129
GET THE REST FROM RESULT => 11 - (129 % 11) = 3

IF RESULT > 9, DIGIT IS 0, ELSE DIGIT IS RESULT.

TO GET SECOND DIGIT FORM LAST SECTION:

1*11 = 11
1*10 = 10
3*9 = 27
3*8 = 21
1*7 = 7
4*6 = 18
3*5 = 15
9*4 = 36
0*3 = 0
3*2 = 6

TOTAL: 11 + 10 + 27 + 21 + 7 + 18 + 15 + 36 + 0 + 6 = 151
GET THE REST FROM RESULT => 151%11 = 5

BONUS:

If the sum pair of all 11 digits are the same, the CPF is invalid.

EXAMPLE:
DIGITS SUM: 1 + 1 + 3 + 3 + 1 + 4 + 3 + 9 + 0 + 3 + 5 = 33 => Is valid.

"""

import re

# WARNING: Disable in production!
debugMode = False


def logThis(message):
    """
    This function is used to log messages if debug is enabled.
    """
    if debugMode:
        print(message)


class CPF_Validator_N:
    """
    This class is used to validate CPF numbers.
    """

    def __init__(self, cpf: str):
        """
        This function is used to initialize the class.
        """
        self.validateCPF(cpf)

    validCPF = None
    partiallyValidation = False

    @staticmethod
    # Validates a CPF number with the easy way.
    def validateCPF(userCPF: str):
        """
        This function is used to validate and clean the CPF number.
        """

        global partiallyValidation

        # regular expression to remove any non-numeric characters, spaces, dots or dashes.
        userCPF = re.sub("[^0-9]", "", userCPF)
        logThis(userCPF)

        # Check length of CPF
        if len(userCPF) != 11:
            validCPF = False
            logThis("CPF is NOT valid.")
            return False
        else:

            # Separate all numbers from userCPF into a list.
            userCPFList = list(userCPF)
            # Sum every integer of the userCPFList
            sumOfDigits = sum(int(i) for i in userCPFList)
            sumOfDigits = str(sumOfDigits)

            #  Get first nine digits from userCPF
            firstNineDigits = userCPFList[0:9]

            # First digit from last section
            sumMaster = 0
            for key, multiply in enumerate(range(len(firstNineDigits) + 1, 1, -1)):
                # logThis(f"{userCPFList[key]} * {multiply}")
                sumMaster += int(userCPFList[key]) * multiply
                # logThis(sumMaster)
            restSum = 11 - (sumMaster % 11)

            # Second Last Digit
            sumMasterSec = 0
            for key, multiply in enumerate(range(len(firstNineDigits) + 2, 1, -1)):
                sumMasterSec += int(userCPFList[key]) * multiply
            restSumSec = 11 - (sumMasterSec % 11)

            if restSum > 9 or restSumSec > 9:
                restSum = 0
                restSumSec = 0

            mergeRes = str(userCPF[:9]) + str(restSum) + str(restSumSec)
            logThis(f"Merged result: {mergeRes}")

            if mergeRes == userCPF and sumOfDigits[0] == sumOfDigits[1]:
                return True
            else:
                logThis(f"CPF is NOT valid.")
                return False


if __name__ == "__main__" and debugMode == True:
    """
    This function is used to run the program.
    """
    if debugMode:
        sampleCPF = "113.314.390-35"
    CPF_Validator_N.validateCPF(sampleCPF)
