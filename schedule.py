from collections import OrderedDict
from pprint import pprint

"""
Methods related to Schedules
"""

def get_schedule(sv):
    # Get Schedule
    schedule = sv.get_schedule().get('StudentClassSchedule').get('TodayScheduleInfoData').get('SchoolInfos').get('SchoolInfo')

    # Get Schedule Type
    school_name = schedule.get('@SchoolName')
    schedule_type = schedule.get('@BellSchedName')
    print(f"{schedule_type} schedule for {school_name} School:")

    # Get Classes
    bell_periods = schedule.get('Classes').get('ClassInfo')

    for bell_period in bell_periods:
        period = bell_period.get('@Period')
        name = bell_period.get('@ClassName')
        room = bell_period.get('@RoomName')
        start = bell_period.get('@StartTime')
        end = bell_period.get('@EndTime')

        print(f"{period}: {name}, Room #{room}, ({start} - {end})")
        
    input()

def get_info_for_class(sv):
    schedule = sv.get_schedule().get('StudentClassSchedule').get('TodayScheduleInfoData').get('SchoolInfos').get('SchoolInfo')
    bell_periods = schedule.get('Classes').get('ClassInfo')
    user_class = int(input("Which class period do you want to check? "))

    try:
        user_class: OrderedDict = bell_periods[user_class]
    except:
        print("Error: Try Again")
        return 1

    period = user_class.get('@Period')
    name = user_class.get('@ClassName')
    room = user_class.get('@RoomName')
    start = user_class.get('@StartTime')
    end = user_class.get('@EndTime')
    teacher = user_class.get('@TeacherName')
    email = user_class.get('@TeacherEmail')

    print(f"Class: {name}\nPeriod: {period}\nRoom #: {room}\nStart Time: {start}\nEnd Time: {end}\nTeacher: {teacher}\nEmail: {email}")
    input()