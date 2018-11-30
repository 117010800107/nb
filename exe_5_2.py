def isOdd(n):
    if num%2==1:
        return Ture
    else:
        return False
while True:
    s = input("Plese enter an Integer:")   
    if not s.isdigit():
        print("Please enter again!")
        continue
    n = eval(s)
if n == -1:
    print("program is over!")
if isOdd(n):
    print("{} is odd".format(n))
else:
     print("{} is even".format(n))
  

    
