class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = self.name[0] + self.last_name + self.birth_year


name_student = input()
last_name_student = input()
birth_year_student = input()

new_student = Student(name_student, last_name_student, birth_year_student)
print(new_student.id)
