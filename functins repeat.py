def take_input():
    varl=-eval(input("Guess the number"))
    return varl

def compare_guess_number(guess_number,secreat_number):
    if(guess_number < secreat_number):
        print("entered number is less than the secret number")
        return False
    elif(guess_number > secreat_number):
        print("entered number is greater than the secret number")
        return False
    else:
        print("the guess number is RIGHT!!!")
        return False
def main():