a=eval(input("enter the string:"))
if(not isinstance(a,str)):
    print("wrong input")
    exit()
else:
    vowels=('a','e','i','o','u')
    for x in a:
        if(x in vowels):
            a=a.replace(x,"")

    print("the string without vowels is :",a)