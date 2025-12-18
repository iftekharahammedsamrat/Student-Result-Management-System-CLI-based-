# Import Important Modules
import json
import os
from colorama import Fore, Style

class Student:
    def __init__(self, name, roll,  marks):
        self.name = name
        self.marks = marks
        self.roll = roll

    def add_student(self):
        # Calculate The Results
        totalmarks = sum(self.marks)
        avg_marks = totalmarks / 3
        AVG_MARKS = f"{avg_marks :.2f}"
        grade = None
        if (avg_marks >= 80):
            grade = "A"
        elif (avg_marks >= 60):
            grade = "B"
        elif (avg_marks >= 40):
            grade = "C"
        else:
            grade = "Fail"
        

        # Combine All Information
        students = {
            "Name" : self.name,
            "Roll" : self.roll ,
            "Marks" : {
                "Bangla" : self.marks[0],
                "English" : self.marks[1],
                "ICT" : self.marks[2]
            },
            "Total Marks" : totalmarks,
            "Average Marks" : AVG_MARKS,
            "Grade" : grade
        }
        # json_data = json.dumps(students)
        
        filename = "data.json"
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            with open("data.json", "r", encoding="utf-8") as file:
                json_student = json.load(file)
        else:
            json_student = []
        
        json_student.append(students)

        # Finally Save the Data 
        with open("data.json", "w", encoding="utf-8") as file:
            json_student_dumps = json.dumps(json_student, indent=4)
            file.write(json_student_dumps)

    def search(rollnumber):
         with open("data.json", "r", encoding="utf-8") as file:
             server_data = json.load(file)
             listlenth = len(server_data)
             for i in range(listlenth):
                 one_file = server_data[i]
                 roll = one_file["Roll"]
                 roll = int(roll)

                #  If Match with Student Roll Number
                 if (rollnumber == roll):
                    print(Fore.GREEN + "Student Found...." + Style.RESET_ALL)
                    # Show The User
                    print("-" * 70)
                    print(f"Student Name : {one_file["Name"]}")
                    print(f"Student Roll : {one_file["Roll"]}")
                    print(f"Total Marks : {one_file["Total Marks"]}")
                    print(f"Average Marks : {one_file["Average Marks"]}")
                    print(f"Grade : {one_file["Grade"]}")




