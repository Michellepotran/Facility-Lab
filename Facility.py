# Defining the facility class
class Facility:
    # Creating the constructor for Facility class
    def __init__(self, fName): # Attributes
        self.fName = fName


# function to display Facilities list
def displayFacilities():
    print("The Hospital Facilities are: \n")
    for i in facilities:
        print(i.fName)


# Function to add new Facility to the list
def addFacility():
    list_length = 1
    for i in range(list_length):
        fName = input("\nEnter Facility name: ")
        facilities.append(Facility(fName))
        
# Function to write Facilities list to facilities.txt
def writeListOffacilitiesToFile():
    with open('facilities.txt', 'w') as f:
        for i in facilities:
            f.write('%s\n' %i.fName)

# Function to display the menu
def facilityMenu():
    while True:
        print("Facilities menu \n 1 - Display Facilities list \n 2 - Add Facility \n 3 - Back to the Main Menu \n")
        category = input()

        if (category == '1'):
            displayFacilities()
        elif (category == '2'):
            addFacility()
        elif (category == '3'):
            writeListOffacilitiesToFile()
            break


facilities = [Facility("Ambulance"), Facility("Admissions"), Facility("Canteen"), Facility("Emergency")]
# User chooses the category
facilityMenu()
