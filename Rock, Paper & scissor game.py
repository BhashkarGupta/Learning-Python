def program():
    import random
    rock = """
    1 - Rock
       _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___) 
    """
    paper = """
    2 - Paper
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """
    scissor = """
    3 - Scissors
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
    user_choice = int(input('''
    Please make your Choice (1, 2, 3) - 
    1. Rock
    2. Paper
    3. Scissors
    '''))
    if user_choice > 3 or user_choice < 1:
        print("Invalid Choice!, Please try again.")
        program()
    else:
        computer_choice = random.randint(1, 3)

        # Print computer selection:
        if computer_choice == 1:
            print(f"""Computer choose: ROCK
            {rock}""")
        elif computer_choice == 2:
            print(f"""Computer choose: PAPER
            {paper}""")
        else:
            print(f"""Computer choose: SCISSORS
            {scissor}""")

        # Print user Selection
        if user_choice == 1:
            print(f"""You choose: ROCK
            {rock}""")
        elif user_choice == 2:
            print(f"""You choose: PAPER
            {paper}""")
        else:
            print(f"""You choose: SCISSORS
            {scissor}""")

        # Making Decision
        if user_choice == computer_choice:
            print("It's a draw!!!")
        elif user_choice == 1:
            if computer_choice == 2:
                print("Sorry, You loose!")
            elif computer_choice == 3:
                print("Yeah, You Win!!!")
        elif user_choice == 2:
            if computer_choice == 3:
                print("Sorry, You loose!")
            elif computer_choice == 1:
                print("Yeah, You Win!!!")
        elif user_choice == 3:
            if computer_choice == 1:
                print("Sorry, You loose!")
            elif computer_choice == 2:
                print("Yeah, You Win!!!")
    replay = input("Wanna play again, Y/N ? - ")
    if replay.lower() == "y":
        program()
    else:
        print("Bye!, See you soon.")


program()
