# ------------------------------------------------------------------------------------------ #
# Title: Assignment04
# Desc: This assignment demonstrates using conditional logic and looping
# Change Log: (Who, When, What)
#   Rabiya Wasiq,11/11/2030,Created Script
# ------------------------------------------------------------------------------------------ #


# Define the Data Constants
MENU: str = '''
----------------------------------------- 
---- Course Registration Program ----
  Select from the following menu:  
    1. View all students registered to date
    2. Register a New Student for a Course
    3. Show New student registration details  
    4. Save New student data to a file
    5. Exit the program

----------------------------------------- 
'''
import json
from json import JSONDecodeError
# Define the Data Variables

student_first_name: str = ''
student_last_name: str = ''
course_name: str = ''
csv_data: str = ''
FILENAME: str = 'Enrollments.json'
file = None
menu_choice: str = ''
second_student: str = ''
student_data: list = []
students: list[dict[str,str]] = []

# Read Data from Json file

try:
    file = open(FILENAME, 'r')
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print(e, e.__doc__, e.__str__(),type(e), sep='\n')
    print('Json file not found, creating it...')
    file = open(FILENAME, 'w')
except JSONDecodeError as e:
    print(e, e.__doc__, e.__str__(), type(e), sep='\n')
    print('Json file does not contain any data, resetting it..')
    file = open(FILENAME, 'w')
    json.dump(students, file)
except Exception as e:
    print('Unexpected Technical error')
    print('-' * 50)
    print(e, e.__doc__, e.__str__(), type(e), sep='\n')
finally:
    if not file.closed:
        file.close()


# Present and Process the data
while True:

    # Present the menu of choices

    print(MENU)

    # Input user data
    menu_choice = input("Please choose an option from the above menu: ")
    print()

    # Menu choice 1 shows the data extracted from the csv and saved in the two-dimensional list
    if menu_choice == "1":
        for student_data in students:
            print(f'Student Full Name :{student_data["First_Name"]} {student_data["Last_Name"]} | Course Name : {student_data["Course_Name"]}')

    # Getting student details from the user

    elif menu_choice == "2":
        while True:
            try:
                student_first_name = input("Enter the student's first name: ").capitalize()
                if not student_first_name.isalpha():
                    raise ValueError('Student First Name can only contain alphabetic characters')
                break
            except ValueError as e:
                print(e)


        while True:
            try:
                student_last_name = input("Enter the student's last name: ").capitalize()
                if not student_first_name.isalpha():
                    raise ValueError('Student First Name can only contain alphabetic characters')
                break
            except ValueError as e:
                print(e)

        course_name = input("Enter the course name: ")

    # Present the current data using f string for string formatting
    elif menu_choice == "3":
        # prompting the user to enter student details in case they skipped a step
        if student_first_name == '' or student_last_name == '' or course_name == '':
            print('Please enter student details again')

        else:
            message = f'{student_first_name} {student_last_name} has registered for {course_name}'
            print(message)


    # Save the data to a file
    elif menu_choice == "4":
        # prompting the user to enter student details in case they skipped a step
        if student_first_name == '' or student_last_name == '' or course_name == '':
            print('Please enter student details again')

        # storing input data as list
        else:
            student_data = {"First_Name": student_first_name, "Last_Name": student_last_name, "Course_Name": course_name}
            students.append(
                student_data)  # adding new student data to the existing data extracted from json file and stored in 2D list


            try:
                file = open(FILENAME, 'w')  # using the write function, to truncate the file
                json.dump(students, file)
                file.close()
                print('Student registration details recorded\n')
            except Exception as e:
                print('Unexpected Technical error')
                print('-' * 50)
                print(e, e.__doc__, e.__str__(), type(e), sep='\n')
            finally:
                if not file.closed:
                    file.close()


    # Stop the loop
    elif menu_choice == "5":
        user_input = input("Do you wish to exit the program?? (Y/N) ").capitalize()
        if user_input == "Y":
            print()
            print('Pausing the program till you press Enter...')
            break

    else:
        print('Incorrect menu choice, please try again')  # incase the user enters the wrong menu-choise
        continue

