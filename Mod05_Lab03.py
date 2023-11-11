# ------------------------------------------------------------------------------------------ #
# Title: Working With Dictionaries And Files
# Desc: Shows how work with dictionaries and files when using a table of data
# Change Log: (Who, When, What)
#   Rabiya Wasiq,11/9/2023,Created Script
# ------------------------------------------------------------------------------------------ #
import json
from typing import TextIO

# Define the Data Constants
FILE_NAME: str = 'MyLabData.csv'

# Define the program's data
MENU: str = '''
---- Student GPAs ------------------------------
  Select from the following menu:  
    1. Show current student data. 
    2. Enter new student data.
    3. Save data to a file.
    4. Exit the program.
-------------------------------------------------- 
'''

student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
student_gpa: float = 0.0  # Holds the GPA of a student entered by the user.
message: str = ''  # Holds a custom message string
menu_choice: str = ''   # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list[dict] = []  # a table of student data
file_data: str = ''  # Holds combined string data separated by a comma.
file :TextIO = None  # Not using type hint helps PyCharm, so we won't use it going forward


# When the program starts, read the file data into a list of dictionary rows (table)

file = open(FILE_NAME, 'r')

# Extract the data from the file
for row in file.readlines():
    row_data = row.split(',')
    student_data = {'First_Name': row_data[0], 'Last_Name':row_data[1],'GPA':float(row_data[2].strip())}
    students.append(student_data)


# Repeat the follow tasks

while True:

    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer.

    # display the table's current data

    if menu_choice == "1":
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            if student["GPA"] >= 4.0:
                message = " {} {} earned an A with a {:.2f} GPA"
            elif student["GPA"] >= 3.0:
                message = " {} {} earned a B with a {:.2f} GPA"
            elif student["GPA"] >= 2.0:
                message = " {} {} earned a C with a {:.2f} GPA"
            elif student["GPA"] >= 1.0:
                message = " {} {} earned a D with a {:.2f} GPA"
            else:
                message = " {} {}'s {:.2f} GPA was not a passing grade"

            print(message.format(student["First_Name"], student["Last_Name"], student["GPA"]))
        print("-" * 50)
        continue

# Add data to the table

    elif menu_choice == "2":
    # Input the data


        try:
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            try:
                student_gpa = float(input("What is the student's GPA? "))
            except ValueError:
                raise ValueError("GPA must be a numeric value.")

            student_data = {"First_Name": student_first_name,
                        "Last_Name": student_last_name,
                        "GPA": float(student_gpa)}
            students.append(student_data)
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')

        continue

    # Save the data to the file
    elif menu_choice == "3":
        #  Save the data to the file
        file = open(FILE_NAME, "w")
        for student in students:
            file.write(f'{student["First_Name"]},{student["Last_Name"]},{student["GPA"]}\n')
        file.close()
        print("Data Saved!")
        continue

    # Exit the program


    elif menu_choice == "4":
        exit_choice =input("Do you want to exit the program (Y/N)").capitalize()
        if exit_choice == 'Y':
            break
        else:
            continue

print(students)

file =open("MyLab01Data.json", 'w')
json.dump(students, file)
file.close()


try:
    file = open("MyLab01Data.json", "r")
    students = json.load(file)
    file.close()
except FileNotFoundError as e:
    print("Text file must exist before running this script!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()


for row in students:
    print(f'First Name: {row["First_Name"]},Last Name: {row["Last_Name"]}')
