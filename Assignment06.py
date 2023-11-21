# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This Assignment Demonstrates Functions and Separation of Concern
# Change Log: (Who, When, What)
#   Rabiya Wasiq,11/18/2023,Created Script
#   Rabiya Wasiq 11/19/2023, Updated I0 function getting_student_data and FileProcessor function writing_data_to_file
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
from typing import TextIO
# Define the Data Variables
FILENAME: str = 'Enrollments.json'
menu_choice: str = ''
new_student: dict = {}
students: list[dict[str,str]] = []


#--------------Processing-----------------

class FileProcessor:

    @staticmethod
    def read_data_from_file( File_Name : str) ->list[dict[str,str,str]]:
        """
        This function reads data from Json file and stores it into a list of dictionaries
        :param File_Name:
        :return: student_data:list[dict[str.str,str]]
        """
        File_Name : str
        student_data : list[dict[str,str,str]]
        file :TextIO = None
        try:
            file = open(File_Name, 'r')
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_message('Json file not found, creating it...',e)
            file = open(File_Name, 'w')
        except JSONDecodeError as e:
            IO.output_error_message('Json file does not contain any data, resetting it..',e)
            file = open(File_Name, 'w')
            json.dump(student_data, file)
        except Exception as e:
            IO.output_error_message('Unexpected Technical error',e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def writing_data_to_file(student_row: dict, students_data:list[dict[str,str,str]], File_Name: str ):
        """
        Writes data to Json file in the format list of dictionaries.
        :param student_row:
        :param students_data:
        :return:
        """
        student_row: dict
        students_data: list[dict[str, str, str]]
        File_Name: str
        file: TextIO = None

        if student_row["First_Name"] == '' or student_row["Last_Name"] == '' or student_row["Course_Name"] == '':
            IO.output_message('Please enter student details again')
        else:
            students_data.append(
                student_row)

        try:
            file = open(File_Name, 'w')  # using the write function, to truncate the file
            json.dump(students, file)
            file.close()
            IO.output_message('Student registration details recorded\n')
        except Exception as e:
            IO.output_error_message('Unexpected Technical error',e)
        finally:
            if not file.closed:
                file.close()


#--------------Presenting----------------------
class IO:

    @staticmethod
    def output_error_message(message : str, error:Exception=None):
        """ This function displays a custom error messages to the user
        default exception value set to none
          :return: None
        """
        print(message, end="\n\n")

        if error is not None:
            print("-- Technical Error Message -- ")
            print('-' * 50)
            print(error, error.__doc__, error.__str__(), type(error), sep='\n')


    @staticmethod
    def output_message(message : str):
        """ This function displays a custom messages to the user
          :return: None
        """
        print(message, end="\n\n")

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu options to the user
        :param menu:
        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        This functions gets the menu choice from the user
        :return: menu_choice
        """
        menu_choice: str
        try:
            menu_choice = input("Enter your menu choice number: ")
            if menu_choice not in ("1", "2", "3", "4","5"):
                raise Exception("Please enter the correct menu choice")
        except Exception as e:
            IO.output_error_messages(e)
        return menu_choice

    @staticmethod
    def current_data_from_file(student_data:list[dict[str,str,str]]) ->str:
        """
        This function displays all student data from the Json file, formatted in a string
        :param student_data:
        :return:
        """
        student_data: list[dict[str, str, str]]
        student_row :dict
        for student_row in student_data:
            IO.output_message(f'Student Full Name :{student_row["First_Name"]} {student_row["Last_Name"]} | Course Name : {student_row["Course_Name"]}')


    @staticmethod
    def input_student_data() -> dict:
        """
        This function gets first name, last name, course name from the user and adds them to a dictionary
        :param student_data:
        :return: student_row
        """
        student_row :dict = {}
        student_first_name: str = ''
        student_last_name: str = ''
        course_name: str = ''

        while True:
            try:
                student_first_name = input("Enter the student's first name: ").capitalize()
                if not student_first_name.isalpha():
                    raise ValueError
                break
            except ValueError:
                IO.output_error_message('Student First Name can only contain alphabetic characters')
                #Not passing error deatils
        while True:
            try:
                student_last_name = input("Enter the student's last name: ").capitalize()
                if not student_last_name.isalpha():
                    raise ValueError
                break
            except ValueError:
                IO.output_message('Student Last Name can only contain alphabetic characters')

        course_name = input("Enter the course name: ")
        student_row = {"First_Name": student_first_name, "Last_Name": student_last_name,
                       "Course_Name": course_name}
        return student_row



    @staticmethod
    def present_student_data(student_row : dict):
        """
        This function presents data from a dictionary to the user in string formatting
        :param student_row:
        :return:
        """
        student_row:dict
        if student_row["First_Name"] == '' or student_row["Last_Name"] == '' or student_row["Course_Name"] == '':
            IO.output_message('Please enter student details again')
        else:
            message = f'{student_row["First_Name"]} {student_row["Last_Name"]} has registered for {student_row["Course_Name"]}'
            IO.output_message(message)

    @staticmethod
    def exit_choice()->str:
        """
        This function presents the user the choice to exit the program
        :return:exit_choice
        """
        exit_choice: str = ''
        exit_choice = input("Do you wish to exit the program? Y/N").capitalize()
        return exit_choice



# Present and Process the data
while True:

    IO.output_menu(menu=MENU)  # Present Menu
    menu_choice = IO.input_menu_choice()

    # Menu choice 1 shows the data extracted from the JSON and saved in the two-dimensional list
    if menu_choice == '1':
        students = FileProcessor.read_data_from_file(File_Name=FILENAME)
        IO.current_data_from_file(student_data=students)

    # Getting student details from the user
    elif menu_choice =='2':
        new_student = IO.input_student_data() #storing new student data as a dictionary to be used later in the program

    #presenting new student registration details to the user
    elif menu_choice =='3':
        IO.present_student_data(student_row=new_student)

    #writing new student details to Json file
    elif menu_choice =='4':
        FileProcessor.writing_data_to_file(student_row=new_student,students_data=students,File_Name=FILENAME)

    #exiting the program
    elif menu_choice == '5':
        exit_choice = IO.exit_choice()
        if exit_choice == "Y":
            IO.output_message('\nPausing the program till you press Enter...\n')
            break
