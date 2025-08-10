try:
    stud_dict = {'Alice': 85, 'Alex': 70, 'Mark': 77, 'Phineas': 88} # dictionary with student names and their makrs
    stud_name = input("Enter the student's name: ") #takes the name of student
    print(stud_dict[stud_name.capitalize()])    # prints the mark of student if name is present
except Exception:
    print("Student not found.") #prints this if student name is not there to avoid error statement
