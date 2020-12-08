from random import randint

while True:
    print("Enter choice:\n 1. Rock\n 2. Paper\n 3. Scissors\n")
    choice = int(input("Enter choice number: \n"))
    while choice>3 or choice<1:
        print("Enter valid input: ")
    #user choice between 1 to 3
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print("User input: " + choice_name)
    #computer choice
    comp = randint(1,3)
    if comp == 1:
        comp_choice = 'Rock'
    elif comp == 2:
        comp_choice = 'Paper'
    else:
        comp_choice = 'Scissors'
    print("Computer's choice: " + comp_choice)
    #condition for winning
    if comp==1:
        if choice == 2:
            print("You win!")
        elif choice == 1:
            print("Tie!")
        else:
            print("You lose!")
    elif comp==2:
        if choice == 1:
            print("You lose!")
        elif choice == 2:
            print("Tie!")
        else:
            print("You win!")
    else:
        if choice == 1:
            print("You win!")
        elif choice == 2:
            print("You lose!")
        else:
            print("Tie!")
    print("Do you want to play again? (y/n)")
    ans = input()
    #exit loop
    if ans == 'n' or ans == 'N':
        break
    
        
        
