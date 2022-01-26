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

    @staticmethod
    def generateCPF():
        """
        This function is used to generate the CPF.
        """

        # Start with random sequence between 0 and 9
        cpf = [random.randrange(10) for _ in range(9)]

        for _ in range(2):
            for i, v in enumerate(cpf):
                res = (len(cpf) + 1 - i) * v

            if res > 9:
                res = 0
            else:
                res = 11 - res

            cpf.append(res)

        return "".join(str(x) for x in cpf)

    def checkCPF():
        if debugMode:
            forceCPF = "113.314.390-35"

        if isThisValid.validateCPF(str(CPF_GEN.generateCPF())) != True:
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
