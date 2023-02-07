from pythonds.basic.stack import Stack

# 只有()的情况
def perChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0 
    
    while index < len(symbolString) and balanced:
                symbol = symbolString[index]
                if symbol == "(":
                        s.push(symbol)
                else:
                        if s.isEmpty():
                                balanced = False
                        else:
                                s.pop()
                index += 1
    if balanced and s.isEmpty():
            return True
    else:
            return False

# 用index来解决匹配的问题，可以尝试用字典
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)

# 多情况考虑
def perChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0 
    
    while index < len(symbolString) and balanced:
                symbol = symbolString[index]
                if symbol == "([{":
                        s.push(symbol)
                else:

                    if s.isEmpty():
                        balanced = False
                    else:
                        top = s.pop()
                        if not matches(top,symbol):
                            balanced=False
                index += 1
    if balanced and s.isEmpty():
            return True
    else:
            return False

dict_ = {'(':')','[':']','{':'}'}