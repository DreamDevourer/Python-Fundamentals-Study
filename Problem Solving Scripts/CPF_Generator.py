#!/usr/bin/env python3

""" Nicolas Mendes - Jan 26 2022

Based on https://www.alura.com.br/conteudo/python-validacao-dados#:~:text=Criando%20um%20novo%20Python%20file,contr%C3%A1rio%20o%20retorno%20ser%C3%A1%20False%20,  https://gist.github.com/lucascnr/24c70409908a31ad253f97f9dd4c6b7c

The CPF calculation is based on the final 2 digits.
To validate, take the first 9 digits of the CPF, generate the 2 digits and save in a new CPF.
Compare if the CPF sent is the same as the CPF generated.
If true, the CPF is valid, otherwise invalid.

SAMPLE CPF: 113.314.390-35
"""

import random
from CPF_Checker import CPF_Validator_N as isThisValid

# WARNING: Disable in production!
debugMode = False


def logThis(message):
    """
    This function is used to log messages if debug is enabled.
    """
    if debugMode:
        print(message)


class CPF_GEN:
    """
    This class is used to generate CPF numbers.
    """

    logThis("Generating CPF...")

    def __init__(self):
        """
        This function is used to initialize the class.
        """
        self.checkCPF()

    @staticmethod
    def generateCPF():
        """
        This function is used to generate the CPF.
        """

        nineDigits = None
        while True:
            nineDigits = [random.randint(0, 9) for i in range(9)]
            if nineDigits != nineDigits[::-1]:
                break

        for i in range(9, 11):
            value = sum((nineDigits[num] * ((i + 1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            nineDigits.append(digit)

        # Start with random sequence between 0 and 9
        result = "".join(map(str, nineDigits))
        logThis(f"Generated CPF: {result}")
        # lastFrst = int(result[-1:])
        # lastSec = int(result[-2:])
        # result = int(result[0:9])

        # result = str(result) + str(lastFrst) + str(lastSec)

        # logThis(f"Generated FINAL CPF: {result}")
        formatGenCPF = f"{result[0:3]}.{result[3:6]}.{result[6:9]}-{result[9:11]}"
        return formatGenCPF

    def checkCPF():

        while (
            isThisValid.validateCPF(CPF_GEN.generateCPF()) != True
            and isThisValid.validateCPF(CPF_GEN.generateCPF()) is not None
        ):
            CPF_GEN.checkCPF()
            logThis(
                f"CPF is invalid, generating another one..."
            )
            # return None
        else:
            logThis(f"CPF is valid! {CPF_GEN.generateCPF()}")
            return CPF_GEN.generateCPF()


if __name__ == "__main__":
    """
    This function is used to run the program.
    """
    # CPF_GEN.checkCPF()
    print(CPF_GEN.checkCPF())
