class Student:

    pass

student_1 = Student()
student_2 = Student()

student_1.first_name = "Gaston"
student_1.last_name = "Quintana"
student_1.major = "Computer Science"

student_2.first_name = "Larissa"
student_2.last_name = "Cuquejo"
student_2.major = "Computer Science"



print(student_1.first_name)
print(student_2.first_name)

class Student:

    school = "Online School"
    numbers_of_students = 0


    def __init__(self, first_name, last_name, major):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        Student.numbers_of_students += 1

    def fullname_with_major(self):
        return f'{self.first_name} {self.last_name} is a' \
               f' {self.major} major!'

    def fullname_major_school(self):
        return f'{self.first_name} {self.last_name} is a' \ 
               f'{self.major} going to {self.school}'

    @classmethod
    def set_online_school(cls, new_school):
        cls.school = new_school

    @classmethod
    def split_students(cls,student_str):
        first_name, last_name, major = student_str.split('.')
        return cls(first_name, last_name, major)



student_1 = Student("Gaston", "Quintana", "Computer Science")
student_2 = Student("Larissa", "Cuquejo", "Computer Science")
new_student = "Leonardo.Cuquejo.Programming"
student_3 = Student.split_students(new_student)


print(f'Number of Students = {Student.numbers_of_students}')
print(student_1.fullname_with_major())
print(student_2.fullname_with_major())
print(f'Number of Students = {Student.numbers_of_students}')
print(student_3.fullname_major_school)




