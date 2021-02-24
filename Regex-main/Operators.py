import random

def kleene(operand):
    repeat = random.randint(0, 5)
    string = ''
    for i in range(repeat):
        string += operand
    return string

def kleenePlus(operand):
    repeat = random.randint(1, 5)
    string = ''
    for i in range(repeat):
        string += operand
    return string

def Concatenation(operand1, operand2):
    return operand1 + operand2

def Or(operand1, operand2):
    return random.choice([operand1, operand2])