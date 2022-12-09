# Storing the facility objects
facilities = ["Ambulance", "Admissions", "Canteen", "Emergency"]

# Defining the facility class
class Facility:

    # Creating the constructor for Facility class
    def __init__(self, fName): # Attributes
        self.fName = fName
#fName = input()

#print("the new facility care is", fName)

# function to display Facilities list
    def displayFacilities():
        print("The Hospital Facilities are: \n")
        for i in facilities:
            print(i)


# Function to add new Facility to the list
    def addFacility():
        list_length = 1
        for i in range (list_length):
            fName = input("\nEnter Facility name: ")
            facilities.append(fName)

# Function to display the menu
    def facilityMenu():
        print("\n 1 - Display Facilities list \n 2 - Add Facility \n 3 - Back to the Main Menu")
        category = input()
        while True:
            if (category in ["1", "2", "3"]):
                return category
            else:
                print("Error, please try again")
                return facilityMenu()

# User chooses the category
    while True:
        category = facilityMenu()
        if (category == '1'):
            displayFacilities()

        elif (category == '2'):
            addFacility()

        elif (category == '3'):
            print("back to the main menu")
            break

        else:
            break



