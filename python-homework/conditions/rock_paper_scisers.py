import random
rock = '''
                _____
            ---'   __)
                    (___)
                    (___)
                    (__)
            ---._(__)
            '''

paper = '''
                _______
            ---'   ____)____
                            __)
                            __)
                            __)
            ---.__________)
            '''

scissors = '''
                _____
            ---'   __)__
                        ____)
                    ________)
                    (__)
            ---._(__)
            '''

user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_selection = random.randint(0, 2)

if user_selection == 1 and computer_selection == 0:
    print(f'User Selection: Paper\n {paper}')
    print(f"Computer Selection: Rock\n {rock}")
    print("You win!")
elif user_selection == 0 and computer_selection == 1:
    print(f'User Selection: Rock\n {rock}')
    print(f"Computer Selection: Paper\n {paper}")
    print("You lose!")
elif user_selection == 0 and computer_selection == 2:
    print(f'User Selection: Rock\n {rock}')
    print(f"Computer Selection: Scissors\n {scissors}")
    print("You win!")
elif user_selection == 2 and computer_selection == 0:
    print(f'User Selection: Scissors\n {scissors}')
    print(f"Computer Selection: Rock\n {rock}")
    print("You lose!")
elif user_selection == 2 and computer_selection == 1:
    print(f'User Selection: Scissors\n {scissors}')
    print(f"Computer Selection: Paper\n {paper}")
    print("You win!")
elif user_selection == 1 and computer_selection == 2:
    print(f'User Selection: Paper\n {paper}')
    print(f"Computer Selection: Scissors\n {scissors}")
    print("You lose!")

elif user_selection == computer_selection:
    print(f"User Selection: {user_selection}")
    print(f"Computer Selection: {computer_selection}")
    print("It's a draw!")
else:
    print("Invalid input, you should input a number between 0 and 2.")