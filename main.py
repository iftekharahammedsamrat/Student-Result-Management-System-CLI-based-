# Import Important Modules
import time
from helper import Student

# Show Option to The users
get_option = None
def showoptions():
    options = '''
    1. Add Student
    2. Show Result
    3. Exit
    '''
    print(options)
    global get_option
    get_option = input("Enter Your Choice :     ")

showoptions()

input_option = None

# Validate User Input
try :
    if  int(get_option):
        input_option = int(get_option)

except :
    print(f"Sorry Invalid Input. Input Must be Number.\nPlease Try Again. If you type worng again you will out form terminal.")
    time.sleep(2)
    showoptions()



# Lets dive into the coding
if (input_option == 1):
    name = input("What is the Student name :      ")
    roll = input("What is the Student roll number :      ")
    print("Please Input Student Marks...")

    bangla = int(input("Bangla : "))
    ict = int(input("ICT : "))
    english = int(input("English : "))
    # Lets Define a Class
    student = Student(name, roll, [bangla, english, ict])
    student.add_student()

elif (input_option == 2):
    roll2 = int(input("Input Your Roll :     "))
    Student.search(roll2)