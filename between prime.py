a=eval(input("enter the 'a' value:"))
if(not isinstance(a,int)):
    print("wrong input")
b=eval(input("enter the 'b' value:"))
if(not isinstance(b,int)):
    print("wrong input")
for num in range(a,b+1):
    if (num>1):
        for i in between  (2,num):
            if((num%i)==0):
                print("prime numbers between 'a' and 'b' are:")
                break
            else:
                print(num)



