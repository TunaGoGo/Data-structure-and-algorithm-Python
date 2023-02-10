def toStr(n,base):
    convertString = "0123456789ABCDEF"

    if n < base:
        return convertString[n]
    else:
        print("------")
        print(convertString[n%base])
        print(toStr(n//base,base))
        return toStr(n//base,base) + convertString[n%base]

print(toStr(444,8))