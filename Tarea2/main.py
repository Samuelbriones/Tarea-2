from Class import University
import os
import time

if __name__ == "__main__":
    
    while True:
        print("╔════════════════════════════════════════╗")
        print("║                  AMG                   ║")
        print("╟────────────────────────────────────────╢")
        print("║ 1.  New Student                        ║")
        print("║ 2.  Show Students                      ║")
        print("║ 3.  New Teacher                        ║")
        print("║ 4.  Show Teachers                      ║")
        print("║ 5.  New Faculty                        ║")
        print("║ 6.  Show Faculties                     ║")
        print("║ 7.  New Career                         ║")
        print("║ 8.  Show Careers                       ║")
        print("║ 9.  New Subject                        ║")
        print("║ 10. Show Subjects                      ║")
        print("║ 11. New Course                         ║")
        print("║ 12. Show Courses                       ║")
        print("║ 13. New Semester                       ║")
        print("║ 14. Show Semesters                     ║")
        print("║ 15. New Grade                          ║")
        print("║ 16. Display All Grades of Students     ║")
        print("║ 17. Exit                               ║")
        print("╚════════════════════════════════════════╝")
        option = input("Enter the option number: ")
        os.system('cls')
        
        match option:
            case "1":
                try:
                    name = input("enter the student name: \n")
                    last_name = input("\nenter the student last name: \n")
                    id = input("\nenter the student identification: \n")
                    
                    while True:
                        tuition = input("\nenter the tuition status of the student [(1) Accepted (2) Rejected]: \n")
                        
                        match tuition:
                            case "1":
                                tuition = True
                                break
                            
                            case "2":
                                tuition = False
                                break
                            
                            case _:
                                print("\nenter a correct option!\n")
                    
                
                    attendance = int(input("\nenter the student's attendance percentage: \n"))
                    
                    student = University.Student(name, last_name, id, tuition, attendance)
                    student.save_student()
                    print("\nStudent saved succesfully!")
                    time.sleep(3)
                    os.system('cls')
        
                except ValueError as err:
                    print("\nthe value entered isn't a number: ", err)
                    time.sleep(3)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')
            
            case "2":
                try:
                    print(University.Student.show_students())
                    time.sleep(8)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')
            
            case "3":
                try:
                    name = input("enter the teacher name: \n")
                    last_name = input("\nenter the teacher last name: \n")
                    id = input("\nenter the teacher identification: \n")
                    
                    teacher = University.Teacher(name, last_name, id)
                    teacher.save_teacher()
                    print("\nTeacher saved succesfully!")
                    time.sleep(3)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')
                    
            case "4":
                try:
                    print(University.Teacher.show_teachers())
                    time.sleep(8)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')
                    
            case "5":
                try:
                    faculty_name = input("Enter the name of new faculty: \n")
                    faculty = University.Faculty(faculty_name)
                    faculty.save_faculty()
                    print("\nFaculty saved succesfully!")
                    time.sleep(3)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')
                    
            case "6":
                try:
                    print(University.Faculty.show_faculties())
                    time.sleep(8)
                    os.system('cls')

                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')
            
            case "7":
                try: 
                    career_name = input("enter the new career name: \n")
                    faculty_name= input("\nenter which faculty the career belongs to: \n")
                    
                    data = University.Faculty.faculty_json()
                    found_faculty = any(faculty.get("faculty") == faculty_name for faculty in data)
                
                    if found_faculty:
                        career = University.Career(career_name, faculty_name)
                        career.save_career()
                        
                        print("\nCareer saved succesfully!")
                        time.sleep(3)
                        os.system('cls')
                    else:
                        print("\nthe faculty entered doesn't exist!")
                        time.sleep(3)
                        os.system('cls')
                        
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')
                    
            case "8":
                try:
                    print(University.Career.show_careers())
                    time.sleep(8)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')
                    
            case "9":
                try:
                    subject_name = input("enter the new subject name: \n")
                    subject_code = input("\nenter the subject code: \n")
                    
                    subject = University.Subject(subject_name, subject_code)
                    subject.save_subject()
                    print("\nSubject saved succesfully!")
                    time.sleep(3)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')
            
            case "10":
                try:
                    print(University.Subject.show_subjects())
                    time.sleep(8)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')    
            
            case "11":
                try:
                    parallel = input("enter the parallel: \n")
                    section = input ("\nenter the section of the parallel: \n")
                    
                    course = University.Course(parallel, section)
                    course.save_course()
                    print("\nCourse saved succesfully!")
                    time.sleep(3)
                    os.system('cls')  
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')  
                    
            case "12":
                try:
                    print(University.Course.show_courses())
                    time.sleep(8)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')  
            
            case "13":
                try:
                    semester_level = input("enter the level of the semester: \n")
                    start_semester = input("\nenter the start date of the semester: \n")
                    end_semester = input("\nenter the end date of the semester: \n")
                    career_name=  input("\nenter the name of the career to which the semester belongs: \n")
                    
                    
                    data = University.Career.career_json()
                    found_career = False
                    
                    for career in data:
                        if career.get("career") == career_name:
                            faculty = career.get("faculty")
                            found_career = True
                            break
                        
                    if found_career:
                        semester = University.Semester(semester_level, start_semester, end_semester, career_name, faculty)
                        semester.save_semester()
                        print("\nSemester saved successfully!")
                        time.sleep(3)
                        os.system('cls')
                    
                    else:
                        print("\nthe career entered doesn't exist")
                        time.sleep(3)
                        os.system('cls')
                    
                except Exception as err:
                    ("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls')  
            
            case "14":
                try:
                    print(University.Semester.show_semesters())
                    time.sleep(8)
                    os.system('cls')
                               
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls') 
                    
            case "15":
                try:
                    id_student = int(input("enter the id of the student: \n"))
                    
                    data = University.Student.students_json()
                    found_student = False
                    
                    for student in data:
                         if student.get("id_student") == id_student:
                            name_student = student.get("name")
                            last_name_student = student.get("last_name")
                            tuition_status = student.get("tuition_status")
                            attendance = student.get("attendance")
                            found_student = True
                            break
                        
                    if found_student:
                        id_semester = int(input("\nenter the id of the semester: \n"))
                        
                        data = University.Semester.semester_json()
                        found_semester = False
                        
                        for semester in data:
                            if semester.get("id") == id_semester:
                                level = semester.get("semester")
                                career = semester.get("career")
                                faculty = semester.get("faculty")
                                found_semester = True
                                break
                        
                        if found_semester:
                            id_course = int(input("\nenter the id of the course: \n"))
                            data = University.Course.course_json()
                        
                            found_course = False
                            
                            for courses in data:
                                if courses.get("id") == id_course:
                                    course = courses.get("parallel")
                                    found_course = True
                                    break
                            
                            if found_course:
                                id_subject = int(input("\nenter the id of the subject: \n"))
                                data = University.Subject.subjects_json()
                                
                                found_subject = False
                                for subject in data:
                                    if subject.get("id") == id_subject:
                                        subject_name = subject.get("subject_name")
                                        found_subject = True
                                        break
                                
                                if found_subject:
                                    id_teacher = int(input("\nenter the id of the teacher: \n"))
                                    data = University.Teacher.teachers_json()
                                    
                                    found_teacher = False
                                    for teacher in data:
                                        if teacher.get("id_teacher") == id_teacher:
                                            name_teacher = teacher.get("name")
                                            last_name_teacher = teacher.get("last_name")
                                            found_teacher = True
                                            break
                                    
                                    if found_teacher:
                                        n1 = float(input("\nEnter note N1: \n"))
                                        n2 = float(input("\nEnter note N2: \n"))
                                        ex1 = float(input("\nEnter note EX1: \n"))
                                        n3 = float(input("\nEnter note N3: \n"))
                                        n4 = float(input("\nEnter note N4: \n"))
                                        ex2 = float(input("\nEnter note EX2: \n"))
                                        re = float(input("\nEnter note RE: \n"))
                                        
                                        grade = University.Grade(name_student, last_name_student, tuition_status, attendance, level, career, faculty, course, subject_name, name_teacher, last_name_teacher, n1, n2, ex1, n3, n4, ex2, re)
                                        grade.save_grade()
                                        
                                        print("\nGrade saved successfully!")
                                        time.sleep(3)
                                        os.system('cls')
                                                                            
                                    else:
                                        print("\nthe teacher doesn't exist!")
                                        time.sleep(3)
                                        os.system('cls')
                        
                                else:
                                    print("\nthe subject doesn't exist!")
                                    time.sleep(3)
                                    os.system('cls')
                                
                            else:
                                print("\nthe course doesn't exist!")
                                time.sleep(3)
                                os.system('cls')
                        
                        else: 
                            print("\nthe semester doesn't exist!")
                            time.sleep(3)
                            os.system('cls')
                            
                    else:
                        print("\nthe student doesn't exist!")
                        time.sleep(3)
                        os.system('cls')
                        
                except ValueError as err:
                    print("\nthe entered value isn't a number!: ", err)
                    time.sleep(3)
                    os.system('cls') 
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls') 
                
            case "16":
                try:
                    print(University.Grade.show_grades())
                    time.sleep(20)
                    os.system('cls')
                    
                except Exception as err:
                    print("\nAn unexpected error has occurred: ", err)
                    time.sleep(3)
                    os.system('cls') 
                    
            case "17":
                break
            
            case _:
                print("Invalid option. Please enter a valid number.")