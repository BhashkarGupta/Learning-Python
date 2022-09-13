# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

X = int(position[0])
Y = int(position[1])
# map[Y - 1][X - 1] = "X"
# could have done this way
if Y == 1:
    row1[X-1] = "X"
elif Y == 2:
    row2[X-1] = "X"
elif Y ==3:
    row3[X-1] = "X"
else:
    print("wrong coordinate")
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

