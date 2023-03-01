print ("Welcome to my computer quiz!")

#Variable used to ask for input
playing = input("Do you want to play? Yes or No ")

#if statement allows us to compare values, true or false
#.lower() converts input to lowercase because Python reads yes and YES differently
if playing.lower() != "yes":
    quit()

print("Okay! Let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("correct")
    score += 1

#if the if statement is not true we can use the else statement
else: print("Incorrect")


answer = input("What does the C in CIA triad stand for ")
if answer.lower() == "confidentiality":
    print("correct")
    score += 1

#if the if statement is not true we can use the else statement
else: print("Incorrect")

answer = input("What is the port number for DNS ")
if answer.lower() == "53":
    print("correct")
    score += 1

#if the if statement is not true we can use the else statement
else: print("Incorrect")

answer = input("What cable is used to connect a node to a router? ")
if answer.lower() == "ethernet":
    print("correct")
    score += 1

#if the if statement is not true we can use the else statement
else: print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")
