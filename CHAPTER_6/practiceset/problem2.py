#write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

math = int(input("Enter the marks of math:"))
physics = int (input("Enter the marks of physics:"))
chemistry = int(input("Enter the marks of chemistry:"))

total_percentage = (100*(math + physics + chemistry))/300
if(total_percentage >= 40 and math >= 33 and physics >= 33 and chemistry >= 33):
    print("You passed.")
else:
    print("You failed.")
    
