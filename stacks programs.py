def stack_push(mylist,element,):
    value=eval(input("enter the element to add\n"))
    mylist.append(value)
    return mylist

def stack_pop(mylist):
    if(len(mylist)!=0):
     mylist.pop()
     return mylist
    else:
        print("the list is empty")

def stack_display(mylist):
    print("the cureent list are:",mylist)
    return mylist

def main():
    print("1 for push  ")
    print("2 for pop")
    print("3 for display")
    print("4 for exit")
    choice = eval(input("enter the choice:"))

    list=[]


    while(True):
        if (choice == 1):
            list1=stack_push(list,choice)
            print("the element added in the list are:\n" , list1)

        elif (choice == 2):
            list2=stack_pop(list)
            print("the element add in the list are:\n" , list2)
        elif (choice == 3):
            list3=stack_display(list)
            print("the element add in the list are:" , list3)
        elif (choice == 4):
            exit()
        else:
            print("enter the coreect value:")

        choice = eval(input("enter the choice:\n"))
    list=list1

main()




