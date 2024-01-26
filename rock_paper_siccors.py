import random
import time

choices = ["rock","paper","scissors"]
cpuchoice = choices[random.randrange(0,2)]
won = "you won!"
lost = "you lost ;("
tie = "tie"
try:
    pinput = int(input("what do you play. rock is 0, paper is 1, and scissors is 2\n"))
except:
    print("not a choice bozo")
pchoice = choices[pinput]
print("computer chose " + str(cpuchoice))
time.sleep(2)
if(cpuchoice == choices[0] and pchoice == choices[2]):
    print(lost)
elif(cpuchoice == choices[0] and pchoice == choices[1]):
    print(won)
elif(cpuchoice == choices[0] and pchoice == choices[0]):
    print(tie)
elif(cpuchoice == choices[1] and pchoice == choices[0]):
    print(lost)
elif(cpuchoice == choices[1] and pchoice == choices[1]):
    print(tie)
elif(cpuchoice == choices[1] and pchoice == choices[2]):
    print(won)
elif(cpuchoice == choices[2] and pchoice == choices[0]):
    print(won)
elif(cpuchoice == choices[2] and pchoice == choices[1]):
    print(lost)
elif(cpuchoice == choices[2] and pchoice == choices[2]):
    print()










