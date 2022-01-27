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


def getDigits(cpf: str):
    """
    This function is used to generate the digits.
    """
    lenQty = len(cpf) + 1
    multiOpr = []
    cpfINT = int(cpf)

    for cpfIndex, multiplyNum in enumerate(range(lenQty, 1)):
        multiOpr.append(int(cpfINT[cpfIndex]) * multiplyNum)
        print(f"{cpf[cpfIndex]} * {multiplyNum} = {multiOpr[cpfIndex]}")

    sumRes = sum(multiOpr)
    finalRes = 11 - (sumRes % 11)

    logThis(f"Final result before: {finalRes}")

    if finalRes > 9:
        finalRes = 0
    else:
        finalRes = finalRes

    logThis(f"Final result: {finalRes}")
    return finalRes


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

    def getDigitOne(cpf: str) -> int:
        return getDigits(cpf[:9])

    def getDigitTwo(cpf: str) -> int:
        return getDigits(cpf[:10])

    @staticmethod
    def generateCPF():
        """
        This function is used to generate the CPF.
        """

        # Start with random sequence between 0 and 9
        nineDigits = "".join([str(random.randint(0, 9)) for x in range(9)])
        digitOne = CPF_GEN.getDigitOne(nineDigits)
        digitTwo = CPF_GEN.getDigitTwo(f"{nineDigits}{digitOne}")
        genCPF = f"{nineDigits}{str(digitOne)}{str(digitTwo)}"
        formatGenCPF = f"{genCPF[0:3]}.{genCPF[3:6]}.{genCPF[6:9]}-{genCPF[9:11]}"
        return formatGenCPF

    def checkCPF():

        if (
            isThisValid.validateCPF(CPF_GEN.generateCPF()) != True
            and isThisValid.validateCPF(CPF_GEN.generateCPF()) is not None
        ):
            # CPF_GEN.generateCPF()
            logThis(
                f"CPF is invalid, generating another one... {CPF_GEN.generateCPF()}"
            )
            return None
        else:
            logThis(f"CPF is valid! {CPF_GEN.generateCPF()}")
            return CPF_GEN.generateCPF()


if __name__ == "__main__":
    """
    This function is used to run the program.
    """
    # CPF_GEN.checkCPF()
    logThis(CPF_GEN.checkCPF())
