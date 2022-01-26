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
debugMode = True


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
        self.generateCPF()

    def getDigits(cpf):
        lenQty = len(cpf) + 1
        for cpfIndex, multiplyNum in enumerate(range(lenQty, 1)):
            cpf = cpf + str(multiplyNum * int(cpf[cpfIndex]))
        return int(cpf) % 11

    def getDigitOne(cpf: str) -> int:
        return CPF_GEN.getDigits(cpf[:9])

    def getDigitTwo(cpf: str) -> int:
        return CPF_GEN.getDigits(cpf[:10])

    @staticmethod
    def generateCPF():
        """
        This function is used to generate the CPF.
        """

        # Start with random sequence between 0 and 9
        nineDigits= "".join([str(random.randint(0, 9)) for x in range(9)])
        digitOne = CPF_GEN.getDigitOne(nineDigits)
        digitTwo = CPF_GEN.getDigitTwo(f"{nineDigits}{digitOne}")
        genCPF = f"{nineDigits}{digitOne}{digitTwo}"

        formatGenCPF = f"{genCPF[0:3]}.{genCPF[3:6]}.{genCPF[6:9]}-{genCPF[9:11]}"
        logThis(f"Test formatted: {formatGenCPF}")

        return formatGenCPF

    def checkCPF():
        if debugMode:
            forceCPF = "113.314.390-35"

        while isThisValid.validateCPF(str(CPF_GEN.generateCPF())) != True:
            CPF_GEN.generateCPF()
            logThis("CPF is invalid, generating another one...")
            # logThis(f"Test Import: {isThisValid.validateCPF(str(CPF_GEN.generateCPF()))}")
            return isThisValid.validateCPF(str(CPF_GEN.generateCPF()))
        else:
            logThis("CPF is valid!")
            return CPF_GEN.generateCPF()


if __name__ == "__main__":
    """
    This function is used to run the program.
    """
    CPF_GEN.generateCPF()
    # CPF_GEN.checkCPF()
    logThis(CPF_GEN.checkCPF())
