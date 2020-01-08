# ITS320 
# Module 8 Portfolio Project
# Robert T. Lancaster
#
# Version 1.5.20-1
#
# Automobile constructor
class Automobile:
    def __init__(self, make, model, color, year, mileage):
        self._make = make
        self._model = model
        self._color = color
        self._year = year
        self._mileage = mileage
        
# Setter\Getter Methods
    def sg_make(self, make = None):
        if make: self._make = make
        return self._make
    def sg_model(self, model = None):
        if model: self._model = model
        return self._model
    def sg_color(self, color = None):
        if color: self._color = color
        return self._color
    def sg_year(self, year = None):
        if year: self._year = year
        return self._year
    def sg_mileage(self, mileage = None):
        if mileage: self._mileage = mileage
        return self._mileage
    def __str__(self):
        return("Make: %s, Model: %s, Color: %s, Year: %s, Mileage: %s" %            
              (self._make, self._model, self._color, self._year, self._mileage))
              
# Inventory constructor
class Inventory:
    def __init__(self):
        self.vehicles = []
# Required methods
    def veh_add(self, veh):
        self.vehicles.append(veh)
    
    def veh_del(self):
        try:
            v_i = int(input("Enter index of vehicle to remove > "))
            select = self.vehicles[v_i]
            print("\nRemoved from Inventory: ",select)
            self.vehicles.remove(select)
        except:
            inv_header = "\nCurrent Vehicle Inventory: "
            print("Entry Error: Returning to Main Menu **")

# Vehicle update method
    def veh_update(self):
        edit_sel = 'd'
        v_i = int(input("Enter index of vehicle to edit > "))
        car2edit = self.vehicles[v_i]
        while True:
            print(edit_menu)
            print("\nEdit mode: ", str(self.vehicles[v_i]))
            edit_choice = input("\nEnter number for attribute to update. (enter \'6\' to quit Edit Mode) > ")
            
            if edit_choice == "1":
                print("Editing make of ", car2edit.sg_make(), car2edit.sg_model())
                car2edit.sg_make(input("Enter new make for > "))
                print("\nVehicle make is set to ", car2edit.sg_make())
            
            elif edit_choice == "2":
                print("Editing model of ", car2edit.sg_make(), car2edit.sg_model())
                car2edit.sg_model(input("Enter new model > "))
                print("\nVehicle model is set to ", car2edit.sg_model())
            
            elif edit_choice == "3":
                print("Editing color of ", car2edit.sg_make(), car2edit.sg_model())
                car2edit.sg_color(input("Enter new color > "))
                print("\nVehicle color is set to" ,car2edit.sg_color())
            
            elif edit_choice == "4":
                print("Editing year of ", car2edit.sg_make(), car2edit.sg_model())
                try:
                    car2edit.sg_year(int(input("Enter new year > ")))
                    print("\nVehicle year is set to ",car2edit.sg_year())
                except:
                    print("\nYear update aborted. Year must be numeric value.")
            
            elif edit_choice == "5":
                print("Editing mileage of ", car2edit.sg_make(), car2edit.sg_model())
                try:
                    car2edit.sg_mileage(int(input("Enter new mileage > ")))
                    print("\nVehicle mileage is set to ", car2edit.sg_mileage())
                except:
                    print("\nMileage update aborted. Mileage must be a numeric value.")    
            
            elif edit_choice == "6":
                print("\n <<< Exiting Edit Mode >>>")
                break
            else:
                print("\n *** Invalid entry. Try again. ***")

# Print inventory           
    def prn_inv(self, inv_header):
        print(inv_header)
        for i in range(len(self.vehicles)):
                 print('%d : ' % i, end = '')
                 print(self.vehicles[i])

# Print file
def export_file(filename, inventory):
        with open(filename, 'w') as f:
           for item in inventory:
               f.write("%s\n" % item)
           

# Edit menu text
edit_menu = """
            <<  Edit Menu >>
            1 - Edit make
            2 - Edit model
            3 - Edit color
            4 - Edit year
            5 - Edit mileage
            6 - End Edit Mode
            """
# Main Menu text
menu = """
     <<<< - Vehicle Inventory: Main Menu - >>>>
        1 - Add a Vehicle
        2 - Delete a Vehicle
        3 - View Inventory
        4 - Update a vehicle in inventory
        5 - Export Inventory to file
        """

# Define main()
    cars = Inventory()
# Program test data
#    cars.veh_add(Automobile('make', 'model', 'color', 0000, 00000))
#   cars.veh_add(Automobile('Nissan', 'Xterra', 'blue', 2004, 89500))
#   cars.veh_add(Automobile('Nissan', 'Maxima', 'silver', 2018, 25000))
#   print(" *** Test data currently in Inventory *** ")
    slotcar = Automobile('Make','Model','Color', 0000, 0000)
    selection = 'd'
    edit_sel = 'd'
    inv_header = "\nCurrent Vehicle Inventory: "
    #cars.prn_inv() 

#.Loop for selection of action
    while selection != 'q':
        cars.prn_inv(inv_header)
        print(menu)

# Choose option from menu
        selection = input("Select an action number. q to quit > ") 
        if selection == "1":
# User input for adding vehicle to inventory
            print("<< Add vehicle to inventory >>")
            make =input("Enter make > ")
            model = input("Enter model > ") 
            color = input("Enter color > ")
            try:
                year = int(input("Enter year > "))
            except ValueError as err:
                print("Invalid year entry - must be a numeric value. Year is set to 1900.", err)
                year = 1900
            try:
                mileage = int(input("Enter mileage > "))
            except ValueError as err:
                print("Invalid mileage entry - Must be a numeric value. Mileage is set to 100.", err)
                mileage = 100
            print("\n")
            slotcar = Automobile(make, model, color, year, mileage)
            cars.veh_add(slotcar)
            print(slotcar.sg_color(),slotcar.sg_year(), slotcar.sg_make(), slotcar.sg_model(), "has been added to inventory.")
# View inventory to get index value to be deleted
        elif selection == "2":
           inv_header = "\nInventory Deletion Mode: "
           cars.prn_inv(inv_header)
           print("\n")
           cars.veh_del()
           inv_header = "\nCurrent Vehicle Inventory: "
# View inventory
        elif selection == "3":
           inv_header = "\nViewing Current Inventory: "
# Edit vehicle in inventory 
        elif selection == "4":
           inv_header = "\nEdit Inventory Unit Mode: "
           cars.prn_inv(inv_header)
           print("\n")
           inv_header = "\nCurrent Vehicle Inventory: "
           try:
               cars.veh_update()
           except:
               inv_header = "\nCurrent Vehicle Inventory: "
               print("\n ** Entry Error: Returning to Main Menu ** ")
# Save list to a user-specified file
        elif selection == '5':
            try:
               filename = input("Enter name of output file (include .txt on the end) > ")
               export_file(filename, cars.vehicles)
               print("\n** Inventory exported to", filename)
            except:
                print("Error: Verify filename is properly specified. ")   
        else:
           print('\n <<< Exiting Vehicle Inventory Program >>>\n')

if __name__ == "__main__": main()

