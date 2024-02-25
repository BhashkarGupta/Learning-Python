#Write your code below this line 👇
def prime_checker(number):
    x = 2
    check = 0
    while x < number:
        if number % x == 0:
            x = number + 1
            check += 1
            print("It's not a prime number.")
        x += 1
    if check == 0 :
        print("It's a prime number.")





#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
