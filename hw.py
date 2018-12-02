def print_persnal_details(*args):
        print("my name is :",args['name'])
        print("my age is:",args['age'])
        print("my loc",args['loc'])
        return

def main():
   name= eval(input("enter the name:"))
    d=[]
    d=['name=jack','age=23','loc=arkeri' ]
    if ('name==jack'):
        print("age is 23")
        print("loc is arkeri")
    else:

      print("the entered name is correct")

main()