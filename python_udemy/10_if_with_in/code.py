number=7
user_input=input("Enter 'y' if you would like to play?: ")

if user_input in ('y',"Y"):
    user_number=int(input("Guess our number: "))
    if user_number==number:
        print("You guessed correctly!!")
    elif user_number-number in (1,-1):
        print("You are off by one.") 
    else: 
        print("Sorry, it's wrong.")