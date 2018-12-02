n= eval(input("enter the multiple of 7"))
if(not isinstance(n,int)):
    print("wrong ans")

if(n<1):
    a = ((n / 7) == 0)
    print("it is multiple of seven")
else:
    print("it is not multiple of seven")

