# Module 2 Critical Thinking
# Robert T. Lancaster
# ITS320_CTA2_Option2.py
#


#import os
car_descr = []
space = " "
lf = "\n"
def main():
#os.system('clear') #removed this because I don't know the OS that my code will be tested on.
#my intent was to clear the display and format my screen output more cleanly.

    print(lf * 2 + space * 5 + "Please respond to the following questions:\n ")
    brand = input(space * 10 + "Enter the brand of your car: ")
    model = input(space * 10 + "Enter the model of your car: ")
    year= input(space * 10 + "Enter the year of your car: ")
    start_odo = input(space * 10 + "Starting odometer reading: ")
    end_odo = input(space * 10 + "Ending odometer reading: ")
    est_mpg = input(space * 10 + "Estimate your mileage per gallon: ")

    car_descr.append({
            "brand": brand,
            "model": model,
            "year": year,
            "start_odo": start_odo,
            "en_odo": end_odo,
            "est_mpg": est_mpg,
            })

# os.system('clear')
    print(lf * 2)
    print(space * 5 + "You entered this information: \n ")
    print(space * 10 + "Brand: " + brand)
    print(space * 10 + "Model: " + model)
    print(space * 10 + "Year: " + year)
    print(space * 10 + "Starting odometer: " + start_odo)
    print(space * 10 + "Ending odometer: " + end_odo)
    print(space * 10 + "Estimated mileage: " + est_mpg)
    print(lf * 5)

if __name__== "__main__":
  main()



# your program should prompt a user to enter a car brand, model, year, starting odometer reading, an ending odometer reading,
# and the estimated miles per gallon consumed by the vehicle. Store your data in a dictionary and print out the contents of the
# dictionary.
