def isNum(num):
    if num.isnumeric():
        return Ture
    elif len(num)==len(set(num)):
        return Ture
    else:
        return False
num=input("")
isnum=isNum(num)
if isnum:
    print("你输入的字符串是数字!")
else:
    print("你输入的字符串不是数字!")
