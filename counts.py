t=eval(input("enter the elements into the tuple"))
if(not isinstance(t,tuple)):
    print("wrong input")
else:
    count=0
    for x in t:
        if (not x%2):
         count +=1
        print("count of the given numbers is ",count)