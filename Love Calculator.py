# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
together = (name1 + name2).lower()
first_number = together.count("t") + together.count("r") + together.count("u") + together.count("e")
second_number = together.count("l") + together.count("o") + together.count("v") + together.count("e")
love_score = first_number * 10 + second_number

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

