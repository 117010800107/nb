def Febric(n):
    if n==1 or n==2:
        return 1
    else:
        return Febric(n-1) + Febric(n-2)

    
