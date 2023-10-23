from abc import ABC
import json
import os
from tabulate import tabulate 

class User(ABC):
    def __init__(self, name, last_name, id):
        self.name = name
        self.last_name = last_name
        self._id = id

    @property
    def id(self):
        return self._id
    
class Student(User):
    _students_json = os.path.join("JSON","Students.JSON")
    def __init__(self, name, last_name, id, tuition_status, attendance):
        super().__init__(name, last_name, id)
        self.tuition_status = tuition_status
        self.attendance = attendance
    
    @property
    def id(self):
        return self._id
    
    def students_json():
        try:
            with open (Student._students_json, "r") as students:
                data = json.load(students)
                
        except json.decoder.JSONDecodeError:
            data = []
            
        return data
    
    def save_student(self):
        data = Student.students_json()
            
        new_student = {
            "id_student": len(data) + 1,
            "name": self.name,
            "last_name": self.last_name,
            "id": self.id,
            "tuition_status": self.tuition_status,
            "attendance": self.attendance
        }
        
        data.append(new_student)
        
        with open (Student._students_json, "w") as students:
            json.dump(data, students)
    
    def show_students():
        data = Student.students_json()
            
        if len(data) <= 0:
            return "No data found in Students.JSON"
        
        else:
            student_table = []
            headers = ["ID Student", "Name", "Last Name", "ID", "Tuition Status", "Attendance"]
            for student in data:
                student_table.append([
                    student["id_student"],
                    student["name"],
                    student["last_name"],
                    student["id"],
                    "Accepted" if student["tuition_status"] else "Rejected",
                    student["attendance"]
                ])

            table = tabulate(student_table, headers, tablefmt="grid")
            
        return table

class Teacher(User):
    _teachers_json = os.path.join("JSON","Teachers.JSON")
    def __init__(self, name, last_name, id):
        super().__init__(name, last_name, id)
        
    @property
    def id(self):
        return self._id
    
    def teachers_json():
        try:
            with open (Teacher._teachers_json, "r") as teachers:
                data = json.load(teachers)
                
        except json.decoder.JSONDecodeError:
            data = []
            
        return data    
    
    def save_teacher(self):
        data = Teacher.teachers_json()
            
        new_teacher = {
            "id_teacher": len(data) + 1,
            "name": self.name,
            "last_name": self.last_name,
            "id": self.id,
        }

        data.append(new_teacher)
        
        with open (Teacher._teachers_json, "w") as teachers:
            json.dump(data, teachers)
    
    def show_teachers():
        data = Teacher.teachers_json()
            
        if len(data) <= 0:
            return "No data found in Teachers.JSON"
        else:
            teacher_table = []
            headers = ["ID Teacher", "Name", "Last Name", "ID"]
            for teacher in data:
                teacher_table.append([
                    teacher["id_teacher"],
                    teacher["name"],
                    teacher["last_name"],
                    teacher["id"]
                ])

            table = tabulate(teacher_table, headers, tablefmt="grid")
            return table

class Subject: 
    _subject_JSON = os.path.join("JSON","Subjects.JSON")
    def __init__(self, subject_name, code):
        self.subject_name = subject_name
        self._code = code
        
    @property
    def code(self):
         return self._code
        
    def subjects_json():
        try:
            with open(Subject._subject_JSON, "r") as subjects:
                data = json.load(subjects)
            
        except json.decoder.JSONDecodeError:
            data = [] 
            
        return data
        
    def save_subject(self):
        data = Subject.subjects_json()
    
        new_subject = {
            "id": len(data)+1,
            "subject_name": self.subject_name,
            "code": self.code
    }
        
        data.append(new_subject)
        
        with open(Subject._subject_JSON, "w") as subjects:
                json.dump(data, subjects)
                
    def show_subjects():
        data = Subject.subjects_json()
        
        if len(data) <= 0:
            return "No data found in Subjects.JSON"
        
        else:
            subject_table = []
            headers = ["ID", "Subject Name", "Code"]
            for subject in data:
                subject_table.append([
                    subject["id"],
                    subject["subject_name"],
                    subject["code"]
                ])

            table = tabulate(subject_table, headers, tablefmt="grid")
            return table

class Course:
    _courses_json = os.path.join("JSON", "Courses.JSON")
    
    def __init__(self, parallel, section):
        self.parallel = parallel
        self.section = section
    
    def course_json():
        try:
            with open (Course._courses_json, "r") as courses:
                data = json.load(courses)
                
        except json.decoder.JSONDecodeError:
            data = []
    
        return data
    
    def save_course(self):
        data = Course.course_json()
        
        new_course = {
            "id": len(data) + 1, 
            "parallel": self.parallel,
            "section": self.section
        }
        
        data.append(new_course)
        
        with open (Course._courses_json, "w") as courses:
                json.dump(data, courses)
    
    def show_courses():
        data = Course.course_json()
            
        if len(data) <= 0:
            return "No data found in Courses.JSON"
        
        else:
            course_table = []
            headers = ["ID", "Parallel", "Section"]
            for course in data:
                course_table.append([
                    course["id"],
                    course["parallel"],
                    course["section"]
                ])

            table = tabulate(course_table, headers, tablefmt="grid")
            return table

class Faculty:
    _faculty_json = os.path.join("JSON", "Faculties.JSON")
    def __init__(self, faculty):
        self.faculty = faculty
    
    def faculty_json():
        try:
           with open (Faculty._faculty_json, "r") as faculties:
               data = json.load(faculties)
               
        except json.decoder.JSONDecodeError:
            data = []
            
        return data
    
    def save_faculty(self):
        data = Faculty.faculty_json()
               
        new_faculty = {
            "id" : len(data) + 1,
            "faculty" : self.faculty
        }
        
        data.append(new_faculty)
        
        with open (Faculty._faculty_json, "w") as faculties:
            json.dump(data, faculties)
            
    def show_faculties():
        data = Faculty.faculty_json()
        
        if len(data) <= 0:
            return "No data found in Faculties.JSON"
        else:
            faculty_table = []
            headers = ["ID", "Faculty"]
            
            for faculty in data:
                faculty_table.append([
                    faculty["id"],
                    faculty["faculty"]
                ])

            table = tabulate(faculty_table, headers, tablefmt="grid")
            return table

class Career(Faculty):
    _careers_json = os.path.join("JSON", "Careers.JSON")
    def __init__(self, career, faculty):
        super().__init__(faculty)
        self.career = career
    
    def career_json():
        try:
            with open (Career._careers_json, "r") as careers:
                data = json.load(careers)
                
        except json.decoder.JSONDecodeError:
                data = []
        
        return data
        
    def save_career(self):
        data = Career.career_json()
                
        new_career = {
            "id": len(data) + 1,
            "career": self.career,
            "faculty": self.faculty
        }

        data.append(new_career)
        
        with open (Career._careers_json, "w") as careers:
            json.dump (data, careers)
            
    def show_careers():
        data = Career.career_json()
                
        if len(data) <= 0:
            return "No data found in Careers.JSON"
        
        else:
            career_table = []
            headers = ["ID", "Career", "Faculty"]
            for career in data:
                career_table.append([
                    career["id"],
                    career["career"],
                    career["faculty"]
                ])

            table = tabulate(career_table, headers, tablefmt="grid")
            return table

class Semester(Career):
    _semesters_json = os.path.join("JSON", "Semesters.JSON")
    
    def __init__(self, semester, start_semester, end_semester, career, faculty):
        super().__init__(career, faculty)
        self.semester = semester
        self.start_semester = start_semester
        self.end_semester = end_semester
     
    def semester_json():
        try:
            with open(Semester._semesters_json, "r") as semesters:
                data = json.load(semesters)
                
        except json.decoder.JSONDecodeError:
            data = []
        
        return data
        
    def save_semester(self):
        data = Semester.semester_json()
            
        new_semester = {
            "id": len(data)+1,
            "semester": self.semester,
            "start_semester": self.start_semester,
            "end_semester": self.end_semester,
            "career": self.career,
            "faculty": self.faculty
        }
        
        data.append(new_semester)
        
        with open(Semester._semesters_json, "w") as semesters:
            json.dump(data, semesters)
            
    def show_semesters():
        data = Semester.semester_json()
                
        if len(data) <= 0:
            return "No data found in Semesters.JSON"
        
        else:
            semester_table = []
            headers = ["Semester", "Start Date", "End Date", "Career", "Faculty"]
            for semester in data:
                semester_table.append([
                    semester["semester"],
                    semester["start_semester"],
                    semester["end_semester"],
                    semester["career"],
                    semester["faculty"]
                ])

            table = tabulate(semester_table, headers, tablefmt="grid")
            return table

class Grade:
    _grades_json = os.path.join("JSON", "Grades.JSON")
    def __init__(self, name_student, last_name_student, tuition_status, attendance, semester, career, faculty, course, subject_name, name_teacher, last_name_teacher, n1, n2, ex1, n3, n4, ex2, re):
        self.name_student = name_student
        self.last_name_student = last_name_student
        self.tuition_status = tuition_status
        self.attendance = attendance
        self.semester = semester
        self.career = career
        self.faculty = faculty
        self.course = course
        self.subject_name = subject_name
        self.name_teacher = name_teacher
        self.last_name_teacher = last_name_teacher
        self.n1 = n1
        self.n2 = n2
        self.ex1 = ex1
        self.n3 = n3
        self.n4 = n4 
        self.ex2 = ex2
        self.re = re
        
    def grade_json():
        try:
            with open (Grade. _grades_json, "r") as grades:
                data = json.load(grades)
        
        except json.decoder.JSONDecodeError:
            data = []
            
        return data
    
    def save_grade(self):
        data = Grade.grade_json()
            
        new_grade = {
            "name_student": self.name_student,
            "last_name_student": self.last_name_student,
            "tuition_status": self.tuition_status,
            "attendance": self.attendance,
            "semester": self.semester,
            "career": self.career,
            "faculty": self.faculty,
            "course": self.course,
            "subject_name": self.subject_name,
            "name_teacher": self.name_teacher,
            "last_name_teacher": self.last_name_teacher,
            "n1": self.n1,
            "n2": self.n2,
            "ex1": self.ex1,
            "n3": self.n3,
            "n4": self.n4,
            "ex2": self.ex2,
            "re": self.re,
            "total": 0,
            "status": ""
            
        }
        
        if new_grade["re"] >= 0:
            
            new_grade["total"] = lambda: round(new_grade["n1"] + new_grade["n2"] + new_grade["ex1"] + new_grade["n3"] + new_grade["n4"] + new_grade["ex2"], 2)
            new_grade["total"] =  new_grade["total"]()
        
        else: 
            
            new_grade["total"] = lambda: round((new_grade["n1"] + new_grade["n2"] + new_grade["ex1"] + new_grade["n3"] + new_grade["n4"] + new_grade["ex2"] + new_grade["re"]) / 2, 2)
            new_grade["total"] =  new_grade["total"]()
        
        if new_grade["tuition_status"] and new_grade["total"] >= 70 and new_grade["attendance"] >= 70:
            
            new_grade["status"] = "Approved"
        
        else:
            new_grade["status"] = "Rejected"          
            
        data.append(new_grade)
        
        with open(Grade. _grades_json, "w") as grades:
            json.dump(data, grades)
        
    def show_grades():
        data = Grade.grade_json()
        
        if len(data) <= 0:
            return "No data found in Grades.JSON"
        
        else:
            grade_table = []
            headers = ["Student Name", "Student Last Name", "Tuition Status", "Semester", "Career", "Faculty", "Parallel", "Subject", "Teacher Name", "Teacher Last Name", "N1", "N2", "EX1", "N3", "N4", "EX2", "RE", "Total", "Status"]
            
            for grade in data:
                tuition_status = "Accepted" if grade["tuition_status"] else "Rejected"
                total = grade["total"]
                status = grade["status"]
                
                grade_table.append([
                    grade["name_student"],
                    grade["last_name_student"],
                    tuition_status,
                    grade["semester"],
                    grade["career"],
                    grade["faculty"],
                    grade["course"],
                    grade["subject_name"],
                    grade["name_teacher"],
                    grade["last_name_teacher"],
                    grade["n1"],
                    grade["n2"],
                    grade["ex1"],
                    grade["n3"],
                    grade["n4"],
                    grade["ex2"],
                    grade["re"],
                    total,
                    status
                ])
            
            table = tabulate(grade_table, headers, tablefmt="grid")
            return table