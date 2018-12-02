def add(num1,num2):
    c=num1+num2
    return c

def main():
    num1=eval(input("enter the first number"))
    num2 = eval(input("enter the second number"))
    c = add(num1,num2)
    print(c)

main()