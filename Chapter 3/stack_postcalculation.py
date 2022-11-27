from pythonds.basic.stack import Stack

def postfixEval(postfixExpr):
    openandStack = Stack()
    tokenlist = openandStack.split()

    for token in tokenlist:
        if token in "0123456789":
            openandStack.push(int(token))
        else:
            openand2 = openandStack.pop()
            openand1 = openandStack.pop()
            result = doMath(token, openand1,openand2)
            openandStack.push(result)
    
    return openandStack.pop()

def doMath(op, op1, op2):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2