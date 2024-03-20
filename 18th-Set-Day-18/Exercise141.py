#Show the user a line of text from your favourite poem and ask for a starting and ending point. Display the characters between those two points. 

fav_poem_line = "It would be well to solder all these pieces back together"

print(fav_poem_line)

start = int(input("Enter a starting number: "))

end = int(input("Enter an ending number: "))

print(fav_poem_line[start:end])