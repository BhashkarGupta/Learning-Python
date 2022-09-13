#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.
toss = random.randint(0,1)
#Write the rest of your code below this line 👇
if toss == 1:
    print("Heads")
else:
    print("Tails")
