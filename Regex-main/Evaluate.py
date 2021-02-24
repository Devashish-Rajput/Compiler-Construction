from RegularExpressionGen import Operators

def evaluate(parseTree):
    opers = {'+' : Operators.kleenePlus,
             '|' : Operators.Or,
             '*' : Operators.kleene,
             '.' : Operators.Concatenation
             }

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        operator = parseTree.getRootVal()
        function = opers[operator]
        if operator == '+' or operator == '*':
            return function(evaluate(leftC))
        else:
            return function(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()
