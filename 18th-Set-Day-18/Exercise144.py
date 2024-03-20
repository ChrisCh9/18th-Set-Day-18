#Ask the user to type in their postcode. Display the first two letters in uppercase.

post_code = input("Enter your postcode: ")

start = post_code[0:2]

print(start.upper())