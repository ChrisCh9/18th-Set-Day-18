#Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep repeating this until they type in a message all in uppercase. 

msg = input("Enter a message in upper case: ")

try_again = False

while try_again == False:
    if msg.isupper():
        print("Thank you")
        try_again = True
    else:
        print("Try again")
        msg = input("Enter a message in upper case: ")