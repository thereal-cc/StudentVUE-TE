from pprint import pprint

"""
Methods related to Student (Background Info)
"""

def get_student_info(sv):
    student_info = sv.get_student_info().get('StudentInfo')
    
    print("What Kind Of Info Would You Like To View?")
    selection = int(input("1. Personal Info\n2. Info related to School\n3. Emergency Contacts\n"))
    print(" ")

    # Personal Info
    if (selection == 1):
        student_name = student_info.get('FormattedName').get('$')
        student_id = student_info.get('PermID').get('$')
        gender = student_info.get('Gender').get('$')
        grade = student_info.get('Grade').get('$')
        address = student_info.get('Address').get('$')
        nickName = student_info.get('NickName').get('$')
        birthDate = student_info.get('BirthDate').get('$')
        email = student_info.get('EMail').get('$')
        phone = student_info.get('Phone').get('$')

        print(f"Name: {student_name}\nID: {student_id}\nGender: {gender}")
        print(f"Current Grade: {grade}\nAddress: {address}\nNickName: {nickName}")
        print(f"Birthday: {birthDate}\nEmail: {email}\nPhone #: {phone}")

    # School Related
    elif (selection == 2):
        # Homeroom
        teacher = student_info.get('HomeRoomTch').get('$')
        email = student_info.get('HomeRoomTchEMail').get('$')
        room = student_info.get('HomeRoom').get('$')

        print(f"Teacher: {teacher}\nEmail: {email}\nRoom #: {room}")

        # Counselor
        counselor_name = student_info.get('CounselorName').get('$')
        counselor_email = student_info.get('CounselorEmail').get('$')

        print(f"Counselor: {counselor_name}\nEmail: {counselor_email}")

    # Health Info
    elif (selection == 3):
        print("Emergency Contacts: ")
        contacts = student_info.get('EmergencyContacts').get('EmergencyContact')
        for contact in contacts:
            name = contact.get('@Name')
            relationship = contact.get('@Relationship')
            phone = contact.get('@HomePhone')
            print(f"Name: {name}\nRelationship: {relationship}\nPhone #: {phone}")

        print("\nPhysician: ")
        physician_info = student_info.get('Physician')
        name = physician_info.get('@Name')
        hospital = physician_info.get('@Hospital')
        phone = physician_info.get('@Phone')
        print(f"Name: {name}\nHospital: {hospital}\nPhone #: {phone}")

        print("\nDentist: ")
        dentist_info = student_info.get('Dentist')
        name = dentist_info.get('@Name')
        office = dentist_info.get('@Office')
        phone = dentist_info.get('@Phone')
        print(f"Name: {name}\nOffice: {office}\nPhone #: {phone}")
        
    else:
        print("Error, Invalid Selection")

    input()

def get_student_attendence(sv):
    return