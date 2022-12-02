# Non user imports
from studentvue import StudentVue
from dotenv import load_dotenv
from pprint import pprint

import sys
import os

# User Imports
from grades import get_overall_grade, get_gradebook
from schedule import get_schedule, get_info_for_class
from student import get_student_info

running = True

def login():
    load_dotenv() # Get This Working
    username = input("StudentVUE Username: ") # Your StudentVUE username
    password = input("StudentVue Password: ") # Your StudentVUE password
    domain = input("School District Domain: ") # Your StudentVUE district's domain
    return StudentVue(username, password, domain)

def main():
    global running
    try:
        sv = login()
    except: 
        print("Error, Login Failed")
        return 1

    print("\nWelcome to StudentVUE (Terminal Edition)!")

    while running:
        print("1. View Gradebook for a Class\n2. View Class Schedule\n3. View Class Info\n4. View Overall Grades\n5. View Student Info\n6. Quit")
        selection = int(input("What would You like to Do? "))

        print(" ")
        if (selection == 1):
            get_gradebook(sv=sv)
        elif (selection == 2):
            get_schedule(sv=sv)
        elif (selection == 3):
            get_info_for_class(sv=sv)
        elif (selection == 4):
            get_overall_grade(sv=sv)
        elif (selection == 5):
            get_student_info(sv=sv)
        elif (selection == 6):
            print("Thank You!")
            running = False
        elif (selection < 0 or selection > 5):
            print("Error, Invalid Option")
            return 1
    
if __name__ == "__main__":
    main()