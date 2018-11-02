str=input("请输入字符串：")
a,b,c,d=0,0,0,0
for i in str:
    if (i>='0')&(i<='9'):
        b=b+1
    elif ((i>='a')&(i<='z'))|((i>='A')&(i<='Z')):
        a=a+1
    elif i==' ':
        c=c+1
    else:
        d=d+1
print("字母个数：{}，数字个数：{}，空格个数：{}，其他字符个数：{}".format(a,b,c,d))

