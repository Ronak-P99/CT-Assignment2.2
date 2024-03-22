'''
You are provided with a Python script that is supposed to guide a user 
through an adventure game, but it has some errors. Identify and fix them.
'''

place = input("Choose a place: forest or cave? ")

if place == "forest": #Added another '='
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree": #Added another '='
        print("You found a bird's nest!")
    elif action == "cross a river": #Changed else to elif and added another '='
        print("You found a boat!")
    else:
        pass

#Task 2:
        
elif place == "cave": #Added another '='
     action = input("light a torch or proceed in the dark? ")
     if action == "light a torch":
         print("You found a hidden treasure!")
     elif action == "proceed in the dark":
        print("Run! Spiders are coming!")
     else:
        pass

#Task 3. I also added passes in the nested 'ifs'
else:
    pass