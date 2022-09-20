# Report comment code

### Introduction to the code using the print function: 
print("This is a code to help you with student comments!") <br> 

### Inputs: You would begin by inputting the answers to the following questions for the code to print a complete comment: 
name=input("What is the student's name? ") <br> 
commitment = input("Describe the student's commitment - begin with the corresponding article (a/an): ") <br> 
twinestory = input("What was the student's twine story? ") <br> 

### Variables for the female pronouns so that it can be inputted in the code (depending on the student's gender) using an f-string: 
f1 = 'She' <br> 
f2 = 'her' <br> 
f3 = 'herself' <br> 

### Variables for the male pronouns so that it can be inputted in the code (depending on the student's gender) using an f-string: 
m1 = 'He' <br> 
m2 = 'his' <br> 
m3 = 'himself' <br> 

### Variables for non-binary pronouns so that it can be inputted in the code (depending on the student's gender) using an f-string:
t1 = 'They' <br> 
t2 = 'theirs' <br> 
t3 = 'themself' <br> 

### Input 1 for student's gender/preferred pronouns: 
gen1 = input("Would you like to use she, he or they? ") <br> 
if gen1 == 'she': <br> 
    gen1 =(f1) <br> 

elif gen1 == 'he': <br> 
    gen1 = (m1) <br> 
<br> 
else: <br> 
    gen1 =(t1) <br> 
    
### Input 2 for student's gender/preferred pronouns:
gen2 = input("Would you like to use her, his or theirs? ") <br> 
if gen2 == 'her': <br> 
    gen2 = (f2) <br> 

elif gen2 == 'his': <br> 
    gen2 = (m2) <br> 

else: <br> 
    gen2 = (t2) <br> 

### Input 3 for student's gender/ preferred pronouns: 
gen3 = input("Would you like to use herself, himself or themself? ") <br> 
if gen3 == 'herself': <br> 
    gen3 = (f3) <br> 

elif gen3 == 'himself': <br> 
    gen3 = (m3) <br> 

else: <br> 
    gen3 = (t3) <br> 
    
### Inputting the student's mark or their project: <br> 
projmark = int(input("What is the student's project mark? ")) <br> 

### Assigning the corresponding comment to the student's mark: 
Assigning the correct comment to the mark: <br> 
if (91<=projmark<=100): <br> 
    projmark = 'an excellent' <br> 

elif (81<=projmark<=90): <br> 
    projmark = 'a most pleasing' <br> 

elif (71<=projmark<=80): <br> 
    projmark = 'a pleasing' <br> 

elif (61<=projmark<=70): <br> 
    projmark = 'a good' <br> 

elif (51<=projmark<=60): <br> 
    projmark = 'a satisfactory' <br> 

### Printing the final comment including all the input and previous coding from above: 
print(f'{name} is a {commitment} student in our Design and Technology class. {gen1} always greets me enthusiastically and endeavours to get on with the task at hand independently. {name} achieved {projmark} result for her interactive {twinestory} Twine story. {gen1} is applying {gen3} well in developing an innovative solution for a client with limited mobility. {name} is demonstrating initiative and curiosity in completing this project and I look forward to {gen2} final product pitch. Keep up the good work, {name}!') 

### Example of the results from the code: <br> 

This is a code to help you with student comments! <br> 
What is the student's name? Veshaya <br> 
Describe the student's commitment - begin with the corresponding article (a/an): an amazing <br> 
What was the student's twine story? Murder mystery <br> 
Would you like to use she, he or they? she <br> 
Would you like to use her, his or theirs? her <br> 
Would you like to use herself, himself or themself? herself <br> 
What is the student's project mark? 90 <br> 
Veshaya is an amazing student in our Design and Technology class. She always greets me enthusiastically and endeavours to get on with the task at hand independently. Veshaya achieved a most pleasing result for her interactive Murder mystery Twine story. She is applying herself well in developing an innovative solution for a client with limited mobility. Veshaya is demonstrating initiative and curiosity in completing this project and I look forward to her final product pitch. Keep up the good work, Veshaya! <br> 

#### You can use the F5 key on IDLE to run the code. 
#### This code was entirely written by Veshaya Pillay with some help from Dr. Muller. <br> 
### Thank you! 
