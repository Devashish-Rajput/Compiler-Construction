from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def ParseTree(exp):
    listCh = exp.split()
    ChStack = Stack()
    expTree = BinaryTree('')

    ChStack.push(expTree)
    currentTree = expTree

    for i in listCh:
        if i == '(':
            currentTree.insertLeft('')
            ChStack.push(currentTree)
            currentTree = currentTree.getLeftChild()

        elif i == ')':
            currentTree = ChStack.pop()

        elif i in ['*', '+', '|', '.']:
            if i not in ['*', '+']:
                currentTree.setRootVal(i)
                currentTree.insertRight('')
                ChStack.push(currentTree)
                currentTree = currentTree.getRightChild()
            else:
                currentTree.setRootVal(i)
                currentTree.insertRight('')
                currentTree.getRightChild().setRootVal('null')

        elif i not in ['*', '+', '|', '.']:
            try:
                currentTree.setRootVal(i)
                parent = ChStack.pop()
                currentTree = parent
            except ValueError:
                pass

    return expTree



