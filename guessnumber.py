'''
guessing game of number'''
import random
computer = random.randint(1,100)
number=-1
guess =0
while(number!=computer):
        guess +=1
        number=int(input("guess the number:"))
        if(number>computer):
             print("lower number please")
             
        else: 
            print("higher number please")
           
print(f"you have guessed right in attempts : {guess}")        
