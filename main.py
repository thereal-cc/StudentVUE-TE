#!/usr/bin/env python

# Non user imports
from studentvue import StudentVue
from dotenv import load_dotenv
from pprint import pprint

# User Imports
from grades import handle_grade_action
from schedule import handle_schedule_action
from student import handle_student_action

running = True

def login():
    load_dotenv() # Get This Working
    print("Enter Credentials: ")
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
    print("Below are some options for general data. Select an option to get more specific Information.")

    while running:
        print("Main Menu:")
        print("1. Schedule\n2. Grades\n3. Student\n4. Quit")
        selection = int(input("Your Choice: "))

        print(" ")
        if (selection == 1):
            handle_schedule_action(sv)
        elif (selection == 2):
            handle_grade_action(sv)
        elif (selection == 3):
            handle_student_action(sv)
        elif (selection == 4):
            print("Thank You!")
            running = False
        elif (selection < 0 or selection > 4):
            print("Error, Invalid Option")
            return 1
    
if __name__ == "__main__":
    main()