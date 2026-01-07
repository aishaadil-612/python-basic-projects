import random 
who = ["Aisha","Shahrukh Khan", "Ayaaz","Justin Beiber", "Selena Gomez","Ranveer Kapoor"]
actions = ["dancing","eating","studying","seeing","staring","quiet","kissing"]
places = ["moscow","newyork", "india ","lucknow","delhi","punjab"]

while True :
    random_who = random.choice(who)
    random_actions = random.choice(actions)
    random_places = random.choice(places)

    sentence = f"{random_who} is {random_actions} in {random_places}"
    print(sentence)
    choice = input("do you want to continue(yes/no):")
    if choice == "no":
        print("ohk good bye then ,tata")
        break


