# Module 4 Critical Thinking
# Robert T. Lancaster
# ITS320_CTA4_Option1.py


space = " "
lf = "\n"

def main():
	
    f = []
    g = []
    rate = 0.2
    interest_value = 0.0
    plusinterest = 0.0
    print(lf * 5)
    print('Please enter floating point values.')
    print(lf * 1)
    for floaty in range(5):
        f.append(float(input("Enter number: ")))
  
    else:
        print(lf * 2)
        print('Total: {}'.format(sum(f)))
 
 # This loop takes the values from list f and adds 20% to each.  Then places them into list g.   
    for value in f:
        interest_value = value * rate
        plusinterest = value + interest_value
        g.append(plusinterest)
        
    print('Average: {}'.format(sum(f)/len(f)))
    print('Maximum: {}'.format(max(f)))
    print('Minimum: {}'.format(min(f)))
    print(lf * 2)
    print("Values entered: ")
    for i in range(len(f)):
        print(space * 8, f[i])
    print(lf)
       	
    print("Values plus interest: ")
    for i in range(len(g)):
        print(space * 8, g[i])
    
    print(lf * 3)
    print("Module 4 Critical Thinking ITS320_CTA4_Option1.py Robert T. Lancaster")
    print(lf)
    
if __name__== "__main__":
  main()









# Option #1: Repetition Control Structure – Five Floating Point Numbers

# Assignment Instructions
# Write a program that utilizes a loop to read a set of five floating-point values from user input. Ask the user to enter the values, then print the following data:

#     Total
#     Average
#     Maximum
#     Minimum
#     Interest at 20% for each original value entered by the user.
#     Use the formula: Interest_Value = Original_value + Original_value*0.2

# Assignment Submission Instructions

#     Submit a text file containing your Python code into the Module 4 drop box. Name your file ITS320_CTA4_Option1.py.
