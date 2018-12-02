principle=eval(input("enter the principle amount"))
time=eval(input("enter the total time(years):"))
rate=eval(input("enter the rate :"))
simple_intrest=(principle*time*rate)/100
print("finally simple interst valu",simple_intrest)
if(rate==0):
    print("simple intrest is zero")

else:
    simple_intrest = (principle * time * rate) / 100
    print("simple intrest ")