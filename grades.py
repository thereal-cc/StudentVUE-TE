from collections import OrderedDict
from pprint import pprint

"""
Methods related to Grades
"""

def get_overall_grade(sv):
    gradebook: OrderedDict = sv.get_gradebook()
    courses: list = gradebook.get('Gradebook').get('Courses').get('Course')
    
    for course in courses:
        print(f"{course.get('@Title')}, {course.get('Marks').get('Mark').get('@CalculatedScoreString')}")

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