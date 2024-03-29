from pythonds.basic.stack import Stack

def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    return binString

#可同时处理十六进制以下的转法
def baseConverter(decNumber,base):
    digits = '0123456789ABCDEF' # 因余数不能直接写两位数，需要查表进行转换。即使16进制，最大余数也只有15，所以到F截至
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    binString = ""
    while not remstack.isEmpty():
        binString = binString + digits[remstack.pop()]
    return binString