#!/usr/bin/env python3

""" Nicolas Mendes - Jan 18 2022

Based on https://programandoautomacao.blogspot.com/2020/10/python-uma-funcao-pythonica-para_15.html

Algorithm for validating CNPJ
For the CNPJ validation, the weights applied to its digits range from 2 to 11. For the CNPJ, the weights range from 2 to 9 and then we reset the weights (again at 2). And, just like for the CNPJ, the weights are applied from right to left.

SAMPLE CNPJ: 46.798.277/0001-02
"""

import re
import sys

# WARNING: Disable in production!
debugMode = False


def logThis(message: str):
    """
    This function is used to log messages if debug is enabled.
    """
    if debugMode:
        print(f"{message}")


def receitaFirstLast():
    """
    This function returns the sequence to discover the first of last two digits.
    """
    return 543298765432


def receitaSecondLast():
    """
    This function returns the sequence to discover the second of last two digits.
    """
    return 6543298765432


class CNPJ_Validator_N:
    """
    This class is used to validate CNPJ numbers.
    """

    def __init__(self, userCNPJ):
        """
        This function is used to initialize the class.
        """
        self.userCNPJ = userCNPJ

    @property
    def validateCNPJ(self):
        """
        This function is used to return the CNPJ validation.
        """
        return self.userCNPJ

    validCNPJ = None
    partiallyValidation = None

    @staticmethod
    # Validates a CNPJ number with the easy way.
    def validateCNPJ(userCNPJ):
        """
        This function is used to validate and clean the CNPJ number.
        """
        # regular expression to remove any non-numeric characters, spaces, dots or dashes.
        userCNPJ = re.sub("[^0-9]", "", userCNPJ)
        logThis(userCNPJ)

        # pick the last 2 digits of userCNPJ.
        last2digits = userCNPJ[-2:]

        # Check length of CNPJ
        if len(userCNPJ) != 14:
            validCNPJ = False
            logThis("CNPJ is NOT valid.")
            return validCNPJ
        else:

            # Separate all numbers from userCNPJ into a list.
            userCNPJList = list(userCNPJ)
            # Sum every integer of the userCNPJList
            sumOfDigits = sum(int(i) for i in userCNPJList)
            sumOfDigits = str(sumOfDigits)

            #  Get first nine digits from userCNPJ
            firstTwelveDigits = userCNPJList[0:12]

            # Let's find the first last digit with this operation.
            # Multiply the last 12 numbers with "543298765432".

            # First digit from last section
            sumMaster = 0
            firstSequenceObj = str(receitaFirstLast())
            firstSequence = []
            firstSequence[:] = firstSequenceObj

            for cnpjNum, eachNum in zip(firstTwelveDigits, firstSequence):
                # logThis(f"{cnpjNum} * {eachNum}")
                sumMaster += int(cnpjNum) * int(eachNum)

            restSum = sumMaster % 11
            logThis(restSum)

            if restSum < 2:
                restSum = 0
            else:
                restSum = 11 - restSum

            # Now let's find the second last digit with this operation.
            # Multiply the last 13 numbers with "6543298765432".

            mergePartRes = str(userCNPJ[:12]) + str(restSum)
            mergeResList = []
            mergeResList[:] = mergePartRes

            secondSequenceObj = str(receitaSecondLast())
            secondSequence = []
            secondSequence[:] = secondSequenceObj

            sumMasterBeta = 0
            for cnpjNum, eachNum in zip(mergeResList, secondSequence):
                # logThis(f"{cnpjNum} * {eachNum}")
                sumMasterBeta += int(cnpjNum) * int(eachNum)
            restSumBeta = sumMasterBeta % 11

            if restSumBeta < 2:
                restSumBeta = 0
            else:
                restSumBeta = 11 - restSumBeta

            mergePartRes = None
            mergePartRes = str(userCNPJ[:12]) + str(restSum) + str(restSumBeta)
            logThis(f"Merged result: {mergePartRes}")

            if mergePartRes == userCNPJ:
                logThis("CNPJ is valid.")
                validCNPJ = True
                return validCNPJ
            else:
                logThis("CNPJ is NOT valid.")
                validCNPJ = False
                return validCNPJ


if __name__ == "__main__":
    """
    This function is used to run the program.
    """
    if debugMode:
        sampleCNPJ = "46.798.277/0001-02"
    CNPJ_Validator_N.validateCNPJ(sampleCNPJ)
