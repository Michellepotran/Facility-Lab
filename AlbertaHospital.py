# Group 13: Michelle, Jerome, Hesed
# 2022-12-15
# this program is a management system customized to meet Alberta Hospital's (AH) need in building
# network of smaller scale mini-hospitals which target underserved rural populations \
# The following criteria are met in this program:
# uses the following classes: Doctor, Facility, Laboratory, Patient, Management
# classes were used to create objects that interact with each other


# file and list global variables

file_for_doctors = 'doctors.txt'
list_of_doctors = []

file_for_laboratories = 'laboratories.txt'
list_of_laboratories = []

file_for_patients = 'patients.txt'
list_of_patients = []

# pass the list from read method


# Doctor class has 6 attributes, 10 methods
class Doctor:

    def __init__(self, pid, name, specialization, working_time, qualification, room_number):
        self.pid = pid
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    # format each doctor's information (properties) in the same format used in the .txt file (has underscores between values)
    def formatDrInfo(self, txt_to_format):
        formatted = '_'.join(txt_to_format)
        return formatted


    # asks the user to enter doctor properties (listed in the properties point)
    def enterDrInfo(self):
        self.readDoctorsFile()
        self.pid = int(input("Enter the doctor’s ID: \n"))
        self.name = input("Enter the doctor’s name: \n")
        self.specialization = input("Enter the doctor’s speciality: \n")
        self.working_time = input("Enter the doctor’s timing (e.g., 7am-10pm): \n")
        self.qualification = input("Enter the doctor’s qualification: \n")
        self.room_number = int(input("Enter the doctor’s room number: \n"))
        list_of_doctors.append([str(self.pid), self.name, self.specialization, self.working_time, self.qualification, str(self.room_number)])
        self.addDrToFile([str(self.pid), self.name, self.specialization, self.working_time, self.qualification, str(self.room_number)])

    # reads from "doctors.txt" file and fills the doctor objects in a list
    def readDoctorsFile(self):
        file = open(file_for_doctors, 'r')
        for each_line in file:
            list_of_doctors.append(each_line.rstrip().split('_'))
        file.close()

    # searches whether the doctor is in the list of doctors/file using the doctor ID that the user enters
    def searchDoctorById(self):
        id_number = int(input("Enter the Doctor's ID: \n"))
        total_rows = len(list_of_doctors)
        current_row = 1
        last_row = total_rows - 1
        doctor_found = ''
        while current_row < total_rows:
            if str(id_number) == list_of_doctors[current_row][0]:
                print(f'{"ID":<5}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' + f'{"Qualification":<17}' + 'Room Number')
                print(f'{list_of_doctors[current_row][0]:<5}' + f'{list_of_doctors[current_row][1]:<15}' + f'{list_of_doctors[current_row][2]:<15}' + f'{list_of_doctors[current_row][3]:<15}' + f'{list_of_doctors[current_row][4]:<17}' + list_of_doctors[current_row][5])
                doctor_found = 'yes'
            if doctor_found != 'yes' and current_row == last_row:
                print("Can't find the doctor with the same ID on the system")
            current_row += 1


    # searches whether the doctor is in the list of doctors/file using the doctor name that the user enters
    def searchDoctorByName(self):
        search_doctor = input("Enter the Doctor's name: \n")
        total_rows = len(list_of_doctors)
        current_row = 1
        last_row = total_rows - 1
        doctor_found = ''
        while current_row < total_rows:
            compare_doctor = list_of_doctors[current_row][1]
            compare_doctor = compare_doctor.replace(' ', '').lower()
            search_doctor = search_doctor.replace(' ', '').lower()
            if search_doctor == compare_doctor:
                print(
                    f'{"ID":<5}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' + f'{"Qualification":<17}' + 'Room Number')
                print(
                    f'{list_of_doctors[current_row][0]:<5}' + f'{list_of_doctors[current_row][1]:<15}' + f'{list_of_doctors[current_row][2]:<15}' + f'{list_of_doctors[current_row][3]:<15}' + f'{list_of_doctors[current_row][4]:<17}' + list_of_doctors[current_row][5])
                doctor_found = 'yes'
            if doctor_found != 'yes' and current_row == last_row:
                print("Can't find the doctor with the same name on the system")
            current_row += 1

    # displays doctor information on different lines, as a list
    def displayDoctorInfo(self):
        for each_row in list_of_doctors:
            print(each_row)

    # asks the user to enter the ID of the doctor to change their information, and then the user can enter the new doctor information
    def editDoctorInfo(self):
        id_number = int(input("Please enter the id of the doctor that you want to edit their information: \n"))
        self.pid = id_number
        total_rows = len(list_of_doctors)
        current_row = 1
        last_row = total_rows - 1
        doctor_found = ''
        self.name = input("Enter new Name: \n")
        self.specialization = input("Enter new Specialist in: \n")
        self.working_time = input("Enter new Timing: \n")
        self.qualification = input("Enter new Qualification: \n")
        self.room_number = int(input("Enter new Room number: \n"))
        while current_row < total_rows:
            if str(id_number) == list_of_doctors[current_row][0]:
                list_of_doctors[current_row][1] = self.name
                list_of_doctors[current_row][2] = self.specialization
                list_of_doctors[current_row][3] = self.working_time
                list_of_doctors[current_row][4] = self.qualification
                list_of_doctors[current_row][5] = str(self.room_number)
                doctor_found = 'yes'
            if doctor_found != 'yes' and current_row == last_row:
                print("Can't find the doctor with the same ID on the system")
            current_row += 1
        self.writeListOfDoctorsToFile()


    # displays all the doctor's information, read from the file, as a report/table
    def displayDoctorsList(self):
        total_rows = len(list_of_doctors)
        current_row = 1
        print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Specialty":<15}' + f'{"Timing":<15}' + f'{"Qualification":<17}' + 'Room Number')
        while current_row < total_rows:
            print(f'{list_of_doctors[current_row][0]:<10}' + f'{list_of_doctors[current_row][1]:<15}' + f'{list_of_doctors[current_row][2]:<15}' + f'{list_of_doctors[current_row][3]:<15}' + f'{list_of_doctors[current_row][4]:<17}' + list_of_doctors[current_row][5])
            current_row += 1


    # writes the list of doctors to the doctors.txt file after formatting it correctly
    def writeListOfDoctorsToFile(self):
        self.readDoctorsFile()
        doctors_file = open(file_for_doctors, 'w')
        for each_line in list_of_doctors:
            line = each_line
            line = self.formatDrInfo(line)
            doctors_file.write(line)
            doctors_file.write('\n')
        doctors_file.close()

    # writes doctors to the doctors.txt file after formatting in correctly
    def addDrToFile(self, new_doctor):
        self.readDoctorsFile()
        doctors_file = open(file_for_doctors, 'a')
        add_line = self.formatDrInfo(new_doctor)
        doctors_file.write(add_line)
        doctors_file.write('\n')
        doctors_file.close()

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
        print("Facilities Menu: \n 1 - Display Facilities list \n 2 - Add Facility \n 3 - Back to the Main Menu \n")
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


# Patient class has 5 properties and 9 methods
class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = int(pid)
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = int(age)

    # formats patient information to be added to the file
    def formatPatientInfo(self, txt_to_format):
        # print("formats patient information to be added to the file")
        formatted = '_'.join(txt_to_format)f
        return formatted

    # asks the user to enter the patient info
    def enterPatientInfo(self):
        self.pid = int(input("Enter patients’s ID: \n"))
        self.name = input("Enter patient’s name: \n")
        self.disease = input("Enter patient's disease: \n")
        self.gender = input("Enter patient's gender: \n")
        self.age = int(input("Enter patient's age: \n"))
        return [str(self.pid), self.name, self.disease, self.gender, str(self.age)]


    # reads from file patients.txt
    def readPatientsFile(self):
        # print("reads from file patients.txt")
        file = open(file_for_patients, 'r')
        list_of_patients = []
        for each_line in file:
            list_of_patients.append(each_line.rstrip().split('_'))
        file.close()
        return list_of_patients

    # searches for a patient using their ID
    def searchPatientByID(self):
        # print("searches for a patient using their ID")
        id_number = int(input("Enter the Patient's ID: \n"))
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = ''
        while current_row < total_rows:
            if str(id_number) == list_of_patients[current_row][0]:
                print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
                print(f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}' + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}' + list_of_patients[current_row][4])
                patient_found = 'yes'
            if patient_found != 'yes' and current_row == last_row:
                print("Can't find the patient with the same ID on the system")
            current_row += 1

    # displays patient info
    def displayPatientInfo(self):
        # print("displays patient info")
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age")
        while current_row < total_rows:
            print(
                f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}' + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}' + list_of_patients[current_row][4])
            current_row += 1

    # writes a list of patients into the patients.txt file
    def writeListOfPatientsToFile(self, list_of_patients):
        print("writes a list of patients into the patients.txt file")
        patients_file = open(file_for_patients, 'w')
        for each_line in list_of_patients:
            add_line = self.formatPatientInfo(each_line)
            patients_file.write(add_line)
            patients_file.write('\n')
        patients_file.close()

    # adds a new patient into the patients.txt file
    def addPatientToFile(self):
        list_of_patients = self.readPatientsFile()
        self.writeListOfPatientsToFile(list_of_patients)
        patient_to_add = self.enterPatientInfo()
        patients_file = open(file_for_patients, 'a')
        patients_file.write(self.formatPatientInfo(patient_to_add))
        patients_file.write('\n')
        patients_file.close()

