n= eval(input("enter the endig number to add for natural numbers"))
if(not isinstance(n,int)):
    print("wrong input")

if  (n>0):
    sum=(n*(n+1))/ 2
    print("sum of the natural is",sum)
else:
    print("error")