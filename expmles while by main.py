def get_upper_list(str1):
    l1=[]
    for idx in str1:
        if(idx.isupper()):
            l1.append(idx)

        return  l1

def get_lower_list(str):
    str1=eval(input("enter the string"))
    l1=[]
    for idx in str1:
        if(idx.isupper()):
            l1.append(idx)

        return  l1

def main():
    str1=eval(input("Enter the string to scan"))
    print("Eneter '1' to scan upper case letters")
    print("Eneter '2' to scan lower case letters")
    print("Eneter '3' to scan upper/lower case letters")
    choice=eval(input("enter your choice"))
    if(choice == 1):
        upper_list = get_upper_list (str1)
        print(upper_list)
    elif(choice == 2):
        lower_list = get_lower_list(str1)
        print(lower_list)
    else:
        upper_list = get_upper_list(str1)
        lower_list = get_lower_list(str1)
        print(upper_list)
        print(lower_list)
main()
