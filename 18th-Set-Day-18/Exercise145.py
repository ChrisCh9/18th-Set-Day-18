#Ask the user to type in their name and then tell them how many vowels are in their name.

name = input("Enter your name: ")

count = 0

name.lower()

for x in name:
    if x=='a' or x=='e' or x=='o' or x=='u' or x=='i':
        count = count + 1
    print("Vowels = ",count)