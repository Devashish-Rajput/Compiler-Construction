from pythonds.basic.stack import Stack
import random
import string

exp = '( ( ( a + null ) | ( b * null ) ) . c )' #Enter regular expression here

Parent = Stack()
Ch = Stack()
Operator = Stack()


def Convert(exp):
    ListExp = exp.split()
    Production = {}
    NonTerminals = list(string.ascii_uppercase)

    for i in ListExp:

        if i == '(':
            Parent.push('(')

        elif i == ')':
            Parent.pop()
            op = Operator.pop()
            right = Ch.pop()
            left = Ch.pop()

            if Parent.isEmpty():
                NT = 'S'
                del NonTerminals[NonTerminals.index('S')]

            else:
                NT = random.choice(NonTerminals)
                del NonTerminals[NonTerminals.index(NT)]

            if op == '|':
                Production[NT] = [left, right]
            elif op == '.':
                Production[NT] = [left+right]
            elif op == '*':
                Production[NT] = [NT+left, 'EPSILON']
            elif op == '+':
                Production[NT] = [left+NT, left]
            Ch.push(NT)
        elif i in ['*', '+', '|', '.']:
            Operator.push(i)
        else:
            Ch.push(i)

    for key in Production.keys():
        print(key, ' --> ', end = '')
        for i in range(len(Production[key])):
            if not (i == len(Production[key]) - 1):
                print(Production[key][i], ' | ', end = '')
            else:
                print(Production[key][i], end = '')
        print()

    print('This is the context free grammar for the given regular expression where S is the start symbol')

Convert(exp)
