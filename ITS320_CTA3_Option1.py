# Module 3 Critical Thinking
# Robert T. Lancaster
# ITS320_CTA3_Option1.py


space = " "
lf = "\n"

def main():
    print('This program will display the approximate value of the Ferrari GTO between the years of 1962 and 2014.')
	
    data_display = 'The value of the GTO for '

    year =  int(input('Enter a year between 1962 and 2014 : '))

    if year < int(1962):
        print(lf * 2 + 'Your entry predates GTO production!' + lf * 4)
    
    elif year >= int(2015) :
	      print(lf * 2 + 'Your date entry is outside of the specified range.' + lf + 'Please enter a year between 1962 and 2014.' + lf * 5)    

    elif int(1962) <= year <= int(1964):
        print(lf * 2 + data_display + str(year) + ' is $18,500.' + lf * 5)
    
    elif int(1965) <= year <= int(1968):
	      print(lf * 2 + data_display + str(year) + ' is $6,000.' + lf * 5)
	  
    elif int(1969) <= year <= int(1971):
	      print(lf * 2 + data_display + str(year) + ' is $12,000.' + lf * 5)
	  
    elif int(1972) <= year <= int(1975):
	      print(lf * 2 + data_display + str(year) + ' is $48,000.' + lf * 5)
	  
    elif int(1976) <= year <= int(1980):
	      print(lf * 2 + data_display + str(year) + ' is $200,000.' + lf * 5)
	  
    elif int(1981) <= year <= int(1985):
	      print(lf * 2 + data_display + str(year) + ' is $650,000.' + lf * 5)
	      
    elif int(1986) <= year <= int(2012):
	      print(lf * 2 + data_display + str(year) + ' is $35,000,000.' + lf * 5)
	      
    elif int(2013) <= year <= int(2014):
	      print(lf * 2 + data_display + str(year) + ' is $52,000,000.' + lf * 5)
	  
	      
print(lf * 5)

if __name__== "__main__":
  main()

# Option #1: Creating a Program to Calculate the Value of a Ferrari
# Assignment Instructions
# Implement a program that reads in a year and outputs the approximate value of a Ferrari 250 GTO
# in that year. Use the following table that describes the estimated value of a GTO at different 
# times since 1962.

# Year	Value
# 1962-1964     $18,500
# 1965-1968	     $6,000
# 1969-1971	    $12,000
# 1972-1975	    $48,000
# 1976-1980	   $200,000
# 1981-1985	   $650,000
# 1986-2012	    $35,000,000
# 2013-2014	    $52,000,000

# (Source: Programming in Python 3 with Zylabs, Chapter 4, Participation Activity 4.3.5)
# Assignment Submission Instructions
# Submit a text file containing your Python code into the Module 3 drop box. Name your file ITS320_CTA3