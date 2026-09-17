#Author: Aditya Raj
#Assignment: Student Marks Analyzer
#Create a simple Student Marks Analyzer using Python
#Requirements:
#Create a list of five subjects
#Take marks of each subject using a for loop
#Store the marks
#Calculate total marks using sum()
#Calculate percentage by dividing total marks by 5
#Use if-elif-else to determine
SEPARATOR="####################################"
GRAY="\033[90m"
RESET="\033[0m"
def marks_analyzer():
    bValueError = False
    def calc_percentage(total_marks):
        if total_subject >= 1 and total_marks >= 0:
            return total_marks / total_subject
        else:
            print(f"{GRAY}[!] Invalid info | @total_subject: {total_subject}, @total_marks: {total_marks}{RESET}")
    def calc_grade(total_percent):
        if total_percent >= 90:
            return "A"
        elif total_percent >= 75:
            return "B"
        elif total_percent >= 60:
            return "C"
        elif total_percent >= 40:
            return "D"
        elif total_percent >= 0 and total_percent <= 39:
            return "Fail"
        else:
            print(f"{GRAY}[!] Invalid percentage: {total_percent}{RESET}")
    subjects = ["Math", "DSA", "Java", "UHV", "OS"]
    total_subject = 5
    max_sub_marks = 100
    total_marks = 0
    print(f"{SEPARATOR}")
    for iter in range(0, total_subject):#iter: 0, 1, 2, 3, 4
        try:
            marks = float(input(f"Enter your {subjects[iter]} Marks: "))
            if marks >= 0 and marks <= max_sub_marks:
                total_marks += marks
            else:
                print(f"{GRAY}[!] Invalid marks: {marks}{RESET}")
                while True:
                    marks = float(input(f"Enter your {subjects[iter]} Marks: "))
                    if marks >= 0 and marks <= max_sub_marks:
                        total_marks += marks
                        break
                    else:
                        print(f"{GRAY}[!] Again invalid marks: {marks}{RESET}")
        except ValueError:
            print(f"{GRAY}[-] You have been chosen a string, process terminated{RESET}")
            bValueError = True
            break
    if not bValueError:
        print(f"{GRAY}[+] Total marks: {total_marks}{RESET}")
        total_percent = calc_percentage(total_marks)
        print(f"{GRAY}[+] Total percentage: {total_percent}{RESET}")
        print(f"{GRAY}[+] Grade: {calc_grade(total_percent)}{RESET}")


marks_analyzer()