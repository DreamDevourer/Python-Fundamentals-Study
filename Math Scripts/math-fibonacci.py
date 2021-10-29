"""
In Mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation:
Fn = Fn-1 + Fn-2
Sample with Seed:
F0 = 0 and F1 = 1
Sequence sample:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377...
"""

fibonacciSequence = [0, 1]


def startUsrInput():
    print("Welcome to the Fibonacci Sequence Calc.")
    fibUsrGift = input("Type a number for the Fibonacci sequence: ")
    fibUsrGift = int(fibUsrGift)
    print(fibonacciFunction(fibUsrGift))


def fibonacciFunction(n):
    if n <= 1:
        print("Not valid.")
    elif n <= len(fibonacciSequence):
        return fibonacciSequence[n-1]
    else:
        fibCalc = fibonacciFunction(n-1) + fibonacciFunction(n-2)
        fibonacciSequence.append(fibCalc)
        return fibCalc


if __name__ == "__main__":
    startUsrInput()