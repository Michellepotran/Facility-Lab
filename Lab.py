# Defining the laboratory class
class Laboratory:
    # Creating the constructor for laboratory class
    def __init__(self, lName, cost): # Attributes
        self.lName = lName
        self.cost = cost

    # formats the lab object similar to the lab .txt file
    def formatLabInfo(self):
        lab_info = f"{self.lName}_{self.cost}"
        return lab_info

    # reads the lab .txt file and fills its contents in a list of lab objects
    def readLaboratoriesFile(self):
        with open(filename, "r") as file:
            for line in file:
                self.lName, self.cost = line.split("_")

    # adds and writes the lab name to the file
    def addLabToFile(self):
        self.lName = input("Enter Laboratory facility: ")
        self.cost = input("Enter Laboratory cost: ")
        lab_info = self.formatLabInfo()

        with open(filename, "a") as file:
            file.write(lab_info + "\n")

# asks user to enter lab name and cost
def enterLaboratoryInfo():
    list_length = 1
    for i in range(list_length):
        lName = input("Enter Laboratory facility: ")
        cost = input("Enter Laboratory cost: ")
        laboratories.append(Laboratory(lName, cost))

# displays the list of labs
def displayLabsList():
    for i in laboratories:
        print(i.lName, i.cost)

# writes the list of labs into file laboratories .txt
def writeListOfLabsToFile():
    with open('laboratories.txt', "w") as f:
        for i in laboratories:
            f.write('%s\n' %i.lName)
            f.write('%s\n' %i.cost)

def labMenu():
    while True:
        print("Laboratories Menu: \n 1 - Display Laboratories list \n 2 - Add Laboratory \n 3 - Back to the Main Menu \n")
        category = input()

        if (category == '1'):
            print("Lab", "Cost")
            displayLabsList()
        elif (category == '2'):
            enterLaboratoryInfo()
        elif (category == '3'):
            writeListOfLabsToFile()
            break


laboratories = [Laboratory("Lab1","800"),Laboratory("Lab2","1200"), Laboratory("Lab3", "500"), Laboratory("Lab4", "50")]
# user chooses the category
labMenu()
