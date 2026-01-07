import random

easy_level = ["cat","dog","ball" ,"ballon","cute"]
mid_level = ["train","aeroplane","computer","study"]
hard_level = ["python","chamelion","arcade"]


print("welcome to the game <3")
print("it is the guessing password game")
level = input("what is your level:")
if level =="hard":
    secret = random.choice(hard_level)
elif level =="easy":
    secret = random.choice(easy_level)
elif level == "medium":
    secret = random.choice(mid_level)  
atempts = 0    
hints = ""  
while True:
    guess = input("guess password:")
    atempts += 1
    if guess == secret:
        print("congratulations")
        break
    for i in range(len(secret)):
       if i<len(guess) and guess[i] == secret[i]:
            hints += guess[i]
       else:
           hints += "_"   

         
    print("hint:",hints)
print("game over")     

