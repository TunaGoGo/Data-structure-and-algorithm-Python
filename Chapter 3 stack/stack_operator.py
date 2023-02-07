from pythonds.basic.stack import Stack

#中缀转后缀
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()#用于储存运算符
    postfixList = []#用于储存除运算符以外的字符
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            opStack.push(token)
        elif token == ")":
            topToken = opStack.pop()#如果是），则从stack中删除一个元素，可能是（，也可能是运算符
            while token != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty) and (prec[opStack.peek()] >= prec[token]):
                opStack.push(token)
    
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return ".".join(postfixList)

