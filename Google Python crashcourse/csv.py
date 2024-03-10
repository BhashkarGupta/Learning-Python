import csv

try:
  with open("username.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      username, identifier, firstName, lastName = row
      print(f"| {username} | {identifier} | {firstName} | {lastName} |")
except FileNotFoundError:
  print("Error: 'username.csv' file not found.")
