import random
import time


characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K',
              'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
              'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
              'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3',
              '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$',
              '%', '&', '*', '(', ')']

alphabetchar =["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K',
               'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
               'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number_char=['1', '2', '3','4', '5', '6', '7', '8', '9', '0']

sign_char=[ '!', '@', '#', '$','%', '&', '*', '(', ')']

print("## WELCOM TO RANDOM PASSWORD ##")

c = int(input("Enter a number of you watn to generate random password: "))
print("1-number")
print("2-alphabet")
print("3-sign")
print("4-all char")

types = int(input("Enter a number of type password: "))
lenth = int(input("Enter a number of lenth password: "))

print("pleas wait ...")

new_password = []
pas2=[]
start_time = time.time()
x=1


if(types==1):
        for x in range(c) :
                while len(new_password) != lenth:
                   new_password.append(number_char[random.randint(0, 9)])
                new_password = "".join(new_password)
                pas2.append(new_password)
                new_password = []
	
if(types==2):
        for x in range(c) :
                while len(new_password) != lenth:
                   new_password.append(alphabetchar[random.randint(0, 51)])
                new_password = "".join(new_password)
                pas2.append(new_password)
                new_password = []

if(types==3):
        for x in range(c) :
                while len(new_password) != lenth:
                   new_password.append(sign_char[random.randint(0, 8)])
                new_password = "".join(new_password)
                pas2.append(new_password)
                new_password = []
        
if(types==4):
        for x in range(c) :
                while len(new_password) != lenth:
                   new_password.append(characters[random.randint(0,70 )])
                new_password = "".join(new_password)
                pas2.append(new_password)
                new_password = []



print ("\n".join(pas2))
print("")
print("________ FINISH ________")
print("")
print("NUMBER PASS GENERTOR : --->> " ,c)
print("")
print("--->>    %s seconds    <<---" % (time.time() - start_time))
print("")

print(" do you want to save password ?? ")
save = input("enter Y or N : ").lower()
if (save=="y"):
        f = open("passfile.txt", "a")
        f.write("\n".join(pas2))
        f.write("\n")
        print(" all password saved ")
        f.close()
else:
        print("password NOT SAVE !!")


input("Press enter to exit ; ")




