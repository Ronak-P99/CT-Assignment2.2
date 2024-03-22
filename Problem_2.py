'''Task 1: Code Correction

You are provided with a Python script that 
is supposed to help in event planning, but it 
has errors. Identify and fix them.

'''

attendees = int(input("Enter number of attendees: ")) #I just added int()
food = input("Would you like vegetarian food? (yes/no) ")

venue = "large hall" if attendees > 100 else "conference room"
print(venue)

'''Task 2: Venue Selection

Based on the corrected code from Task 1, 
further enhance the program to recommend 
additional facilities like "audio system" or 
"projector" based on the number of attendees.

'''
if venue == "large hall":
    print("You are eligible for both an audio system and a projector")
elif venue == "conference room":
        tech = input("You can choose between an audio system or a projector. Which would you like? ")
        if tech == "projector":
              print("Your projector is all set!")
        elif tech == "audio system":
              print("Your audio system is all set!")

'''

Task 3: Catering Choices
Ask the user if they want "vegetarian" food. 
Recommend "Veggie Delight Caterers" if yes, 
otherwise recommend "Gourmet Meals Caterers"

'''
type_food = "We will provide Veggie Delight Caters" if food == "yes" else "We will provide Gourmet Meals Caterers!"
print(type_food)