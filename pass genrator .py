import random
import time

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*', '(', ')']

c = int(input("Enter a number: "))
new_password = []
start_time = time.time()
x=1
for x in range(c) :
	while len(new_password) != 30:
		new_password.append(characters[random.randint(1, 70)])
	new_password = "".join(new_password)
	print(x+1,"_", new_password)
	new_password = []	


print("")
print("      @@@@   ________ FINISH ________    @@@@   ")
print("")
print("NUMBER PASS GENERTOR : " ,c)
print("")
print("---    %s seconds    ---" % (time.time() - start_time))




