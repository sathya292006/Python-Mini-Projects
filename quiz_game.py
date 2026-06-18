print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")

if playing.lower()!="yes":
    quit()

print("Okay! Let's play:)")

Score=0
#1
answer=input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print('correct')
    Score+=1
else:
    print("Incorrect!")

#2
answer=input("What does GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print('correct')
    Score+=1
else:
    print("Incorrect!")

#3
answer=input("What does RAM stands for? ")
if answer.lower()=="random access memory":
    print('correct')
    Score+=1
else:
    print("Incorrect!")

#4
answer=input("What does PSU stands for? ")
if answer.lower()=="power supply":
    print('correct')
    Score+=1
else:
    print("Incorrect!")


print("You got " + str(Score) + " questions correct!")

print("You got " + str((Score/4)*100) + "%.")