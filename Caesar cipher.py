logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
print(logo)


def encode(plain_string, shift):
    plain_list = []
    encrypted_string = ""
    # Extracting letter to a list
    for plain_letter in plain_string:
        plain_list.append(plain_letter.lower())
    # Shifting letter as per defined shift
    for plain_letter in plain_list:
        if plain_letter not in alphabet:
            encrypted_string += plain_letter
        else:
            encrypted_string += alphabet[(shift + alphabet.index(plain_letter)) % 26]
    # returning encrypted text
    return encrypted_string


def decode(encrypted_string, shift):
    encode_list = []
    decrypted_string = ""

    # Creating list for encrypted string
    for letter in encrypted_string:
        encode_list.append(letter)
    # Shifting letter as per shift to decrypt
    for encrypted_letter in encode_list:
        if encrypted_letter not in alphabet:
            decrypted_string += encrypted_letter
        else:
            decrypted_string += alphabet[(alphabet.index(encrypted_letter) - shift) % 26]
    return decrypted_string


def program():
    select_function = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if select_function == "encode" or select_function == "decode":
        string = input("Type your message:\n")
        shift = int(input("Type the shift number.\n"))
        if select_function == "encode":
            encrypted_string = encode(string, shift)
            print("Here's the encoded result: {}".format(encrypted_string))
            start_again()
        elif select_function == "decode":
            decrypted_string = decode(string, shift)
            print("Here's the decoded result: {}".format(decrypted_string))
            start_again()
    else:
        print("Invalid selection. Please try again.")
        program()


def start_again():
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if again == "yes":
        program()
    elif again == "no":
        print("Thank you for using my cipher program. :-)")
    else:
        print("Wrong input. Please try again.")
        start_again()


program()


# logo = """
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
#             88             88
#            ""             88
#                           88
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
# 8b         88 88       d8 88       88 8PP""""""" 88
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
#               88
#               88
# """
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
# print(logo)
#
#
# def encode(plain_string, shift):
#     plain_list = []
#     encrypted_string = ""
#     # Extracting letter to a list
#     for plain_letter in plain_string:
#         plain_list.append(plain_letter.lower())
#     # Shifting letter as per defined shift
#     for plain_letter in plain_list:
#         if plain_letter not in alphabet:
#             encrypted_string += plain_letter
#         else:
#             encrypted_string += alphabet[(shift + alphabet.index(plain_letter)) % 26]
#     # returning encrypted text
#     return encrypted_string
#
#
# def decode(encrypted_string, shift):
#     encode_list = []
#     decrypted_string = ""
#
#     # Creating list for encrypted string
#     for letter in encrypted_string:
#         encode_list.append(letter)
#     # Shifting letter as per shift to decrypt
#     for encrypted_letter in encode_list:
#         if encrypted_letter not in alphabet:
#             decrypted_string += encrypted_letter
#         else:
#             decrypted_string += alphabet[(alphabet.index(encrypted_letter) - shift) % 26]
#     return decrypted_string
#
#
# def program():
#     select_function = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
#     if select_function == "encode" or select_function == "decode":
#         string = input("Type your message:\n")
#         shift = int(input("Type the shift number.\n"))
#         if select_function == "encode":
#             encrypted_string = encode(string, shift)
#             print("Here's the encoded result: {}".format(encrypted_string))
#             start_again()
#         elif select_function == "decode":
#             decrypted_string = decode(string, shift)
#             print("Here's the decoded result: {}".format(decrypted_string))
#             start_again()
#     else:
#         print("Invalid selection. Please try again.")
#         program()
#
#
# def start_again():
#     again = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
#     if again == "yes":
#         program()
#     elif again == "no":
#         print("Thank you for using my cipher program. :-)")
#     else:
#         print("Wrong input. Please try again.")
#         start_again()
#
#
# program()
