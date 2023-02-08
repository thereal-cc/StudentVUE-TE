from collections import OrderedDict

"""
Methods related to Schedules
"""

def handle_schedule_action(sv):
    print("Get To Know Your Schedule!")
    print("1. View Schedule\n2. View Info for a Specific Class")
    selection = int(input("Your Choice: "))
    print(" ")
    if (selection == 1):
        get_schedule(sv=sv)
    elif (selection == 2): 
        get_info_for_class(sv=sv)
    else:
        print("Error, Invalid Selection")
        return 1

def get_schedule(sv):
    # Get Schedule
    schedule = sv.get_schedule().get('StudentClassSchedule').get('TodayScheduleInfoData').get('SchoolInfos').get('SchoolInfo')

    # If there's school today
    if schedule is not None:
        # Get Schedule Type
        school_name = schedule.get('@SchoolName')
        schedule_type = schedule.get('@BellSchedName')
        print(f"{schedule_type} schedule for {school_name} School:")

        # Get Classes
        bell_periods = schedule.get('Classes').get('ClassInfo')

        # Each Class
        for bell_period in bell_periods:
            period = bell_period.get('@Period')
            name = bell_period.get('@ClassName')
            room = bell_period.get('@RoomName')
            start = bell_period.get('@StartTime')
            end = bell_period.get('@EndTime')

            print(f"{period}: {name}, Room #{room}, ({start} - {end})")
    else: 
        print("Looks like you don't have School today...\nWe can't give you times, but here are your classes: ")
        schedule = sv.get_schedule().get('StudentClassSchedule').get('ClassLists')
        bell_periods = schedule.get('ClassListing')

        for bell_period in bell_periods:
            period = bell_period.get('@Period')
            name = bell_period.get('@CourseTitle')
            room = bell_period.get('@RoomName')

            print(f"{period}: {name}, Room #{room}")

        # pprint(bell_periods)

    input()

def get_info_for_class(sv):
    schedule = sv.get_schedule().get('StudentClassSchedule').get('TodayScheduleInfoData').get('SchoolInfos').get('SchoolInfo')

    if schedule is not None:
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
    else:
        schedule = sv.get_schedule().get('StudentClassSchedule')
        bell_periods = schedule.get('ClassLists').get('ClassListing')
        user_class = int(input("Which class period do you want to check? "))

        try:
            user_class: OrderedDict = bell_periods[user_class]
        except:
            print("Error: Try Again")
            return 1

        period = user_class.get('@Period')
        name = user_class.get('@CourseTitle')
        room = user_class.get('@RoomName')
        teacher = user_class.get('@Teacher')
        email = user_class.get('@TeacherEmail')

        print(f"Class: {name}\nPeriod: {period}\nRoom #: {room}\nTeacher: {teacher}\nEmail: {email}")

    input()