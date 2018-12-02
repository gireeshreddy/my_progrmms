n=eval(input("enter the n value:"))
if(not isinstance(n,int)):
    print("wrong input")
else:
  fact=1
  while(n>0):
    fact=fact*n
    n=n-1
print("The factorial of the number is",fact)