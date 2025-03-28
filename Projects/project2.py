# Beginning: create variables
liv_points = 0
maddie_points = 0

# Middle: ask questions
answer= input("Which hobby would you prefer A) playing basketball, or B) or singing?")
if answer == "A":
    maddie_points += 1
elif answer == "B":
    liv_points += 1


answer = input("Do you like A) high heels, or B) sneakers?")
if answer == "A":
    liv_points += 1
elif answer == "B":
    maddie_points += 1


answer = input("Are you more A) outgoing, or B) competitive?")
if answer == "A":
    liv_points += 1
elif answer == "B":
    maddie_points += 1


answer = input("Would you rather A) watch sports, or B) watch a musical?")
if answer == "A":
    maddie_points += 1
elif answer == "B":
    liv_points += 1


answer = input("Would you rather A) live in hollywood, or B) live in wisconsin?")
if answer == "A":
    liv_points += 1
elif answer == "B":
    maddie_points += 1


# end of quiz:
if liv_points > maddie_points:
    print ("you are more like liv!")
elif maddie_points > liv_points:
    print ("you are more like maddie!")
