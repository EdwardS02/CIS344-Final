import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="teachers_portal",
                 user='root',
                 password='Test@123'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                return
        except Error as e:
            print("Error while connecting to MySQL", e)
    

    def getAllStudents(self):
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            self.cursor.callproc("studentsWithGrade")
            records = self.cursor.stored_results()
            return records

    def addStudent(self, name, courseID, grade):
        new_student = ("INSERT INTO students (studentName, enrolledInCourseID, grade) "
                       "VALUES (\"" +name+ "\", " +courseID+", " +grade+")")
        cursor = self.connection.cursor()
        cursor.execute(new_student)
        self.connection.commit()
        cursor.close()
        
    def addCourse(self, name):
        ''' Complete the method to insert a course to
        course table'''
        cursor = self.connection.cursor()
        new_course = "INSERT INTO courses (courseName) VALUES (%s)"
        cursor.execute(new_course, (name,))
        self.connectionn.commit()
        cursor.close()

    def searchStudent(self, name):
        cursor = self.connection.cursor()
        search_student = "INSERT INTO students (studentId) VALUES (%s)"
        cursor.execute(search_student, (name,))
        self.connectionn.commit()
        cursor.close()
    
    def modifyGrade(self, studentID, grade):
        ''' Complete the method to update the grade of the student'''
        pass
        
        
        
    
    
