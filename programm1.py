principal=eval(input("enter the principle amount"))
time=eval(input("enter the total time(years):"))
rate=eval(input("enter the rate value:"))

if (rate == 0):
    print("simple interest is zero")

else:
    simple_intrst = (principal * time * rate) / 100
    print("finally simple interst value:", simple_intrst)
