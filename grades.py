from collections import OrderedDict

"""
Methods related to Grades
"""

def handle_grade_action(sv):
    print("Info Related To Grades!")
    print("1. View Gradebook for a Class\n2. View Overall Grades")
    selection = int(input("Your Choice: "))
    print(" ")
    if (selection == 1):
        get_gradebook(sv=sv)
    elif (selection == 2): 
        get_overall_grades(sv=sv)
    else:
        print("Error, Invalid Selection")
        return 1

def get_overall_grades(sv):
    gradebook: OrderedDict = sv.get_gradebook()
    courses: list = gradebook.get('Gradebook').get('Courses').get('Course')

    for course in courses:
        print(f"{course.get('@Period')}: {course.get('@Title')}, {course.get('Marks').get('Mark').get('@CalculatedScoreString')}")
    
    input()

def get_gradebook(sv):
    gradebook: OrderedDict = sv.get_gradebook()
    courses: list = gradebook.get('Gradebook').get('Courses').get('Course')
    
    period = int(input("Which period's gradebook do you want to view? "))

    try:
        course = courses[period - 1]
    except:
        print("Error, Period is not available")
        return 1

    # Print General Info
    name = course.get('@Title')
    overall_grade = course.get('Marks').get('Mark').get('@CalculatedScoreRaw')
    print(f"{name}\nOverall Grade: {overall_grade}")

    # Return List of Assignments
    try:
        print(f"Assignments: ")
        assignments = course.get('Marks').get('Mark').get('Assignments').get('Assignment')
        for assignment in assignments:
            assignment_name = assignment.get('@Measure')
            assignment_type = assignment.get('@Type')
            assignment_score = assignment.get('@Score')

            print(f"{assignment_name}\n\t{assignment_type}\n\tScore: {assignment_score}")
    except:
        print("Error, Grades are not public yet!")
        return 1

    input()