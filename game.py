import random
'''
snake = 2
water = 1
gun= 3
'''
computer = random.choice([2,3,1])
youstr = input("enter your choice =")
youDict = { "snake":2 , "water": 1 , "gun" : 3}
reversedict = { 2 :"snake" , 1 : "water" , 3 : " gun" }
you = youDict[youstr]
print (f"you chose {reversedict[you]} and computer chose {reversedict[computer]}")
if(you == computer):
    print("its a draw")
else:
    if(computer == 1 and you == 2 ): 
        print ("you won")
    elif(computer == 1 and you == 3 ):
        print ("you lose") 
    elif(computer == 2 and you == 3 ):
        print ("you win") 
    elif(computer == 2 and you == 1 ):
        print ("you lose") 
    elif(computer == 3 and you == 1 ):
        print ("you win")             
    elif(computer == 3 and you == 2 ):
        print ("you lose")  
    else :
        print("its a wrong")
    