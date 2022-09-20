print("This is a code to help you with student comments!") 

name=input("What is the student's name? ")
commitment = input("Describe the student's commitment - begin with the corresponding article (a/an): ")
twinestory = input("What was the student's twine story? ")

f1 = 'She'
f2 = 'her'
f3 = 'herself'

m1 = 'He'
m2 = 'his'
m3 = 'himself'

t1 = 'They'
t2 = 'theirs'
t3 = 'themself'


gen1 = input("Would you like to use she, he or they? ")
if gen1 == 'she':
    gen1 =(f1)

elif gen1 == 'he':
    gen1 = (m1)

else:
    gen1 =(t1)
    
gen2 = input("Would you like to use her, his or theirs? ")
if gen2 == 'her':
    gen2 = (f2)

elif gen2 == 'his':
    gen2 = (m2)

else:
    gen2 = (t2)


gen3 = input("Would you like to use herself, himself or themself? ")
if gen3 == 'herself':
    gen3 = (f3)

elif gen3 == 'himself':
    gen3 = (m3)

else:
    gen3 = (t3) 
    
projmark = int(input("What is the student's project mark? "))

if (91<=projmark<=100):
    projmark = 'an excellent'

elif (81<=projmark<=90):
    projmark = 'a most pleasing'

elif (71<=projmark<=80):
    projmark = 'a pleasing'

elif (61<=projmark<=70):
    projmark = 'a good'

elif (51<=projmark<=60):
    projmark = 'a satisfactory'



print(f'{name} is {commitment} student in our Design and Technology class. {gen1} always greets me enthusiastically and endeavours to get on with the task at hand independently. {name} achieved {projmark} result for her interactive {twinestory} Twine story. {gen1} is applying {gen3} well in developing an innovative solution for a client with limited mobility. {name} is demonstrating initiative and curiosity in completing this project and I look forward to {gen2} final product pitch. Keep up the good work, {name}!') 


