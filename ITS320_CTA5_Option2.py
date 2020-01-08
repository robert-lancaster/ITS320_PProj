# Module 5 Critical Thinking
# Robert T. Lancaster
# ITS320_CTA5_Option2.py

# define string processing function
def catfun(st1, st2, st3):
       
    print("String 3 reversed: ",st3[::-1])
    
    return st1 + " " + st2

lf = "\n"

# define main function
def main():

    s1 = input("Enter a string:")

    s2 = input("Enter another string:")

    s3 = input("Enter the last string:")
    print(lf * 2)
    
# call string processing function
    s4 = catfun(s1, s2, s3)
    print("Combined string 1 and 2:", s4)

if __name__== "__main__":
  main()

