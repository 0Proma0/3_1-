class Student():
    def __init__(self, name, age, program):
        self.name = name
        self.age = age
        self.program = program
        self.grades = []
        
    def introduce(self):
        print(f'Hi, nazywam się {self.name}, studjuję {self.program} i mam {self.age} lat')
    
    def recive_grade(self, grade):
        self.grades.append(grade)
    
    def __lt__(self,friend):
        self.mean = 0
        friend.mean = 0
        for grade in self.grades:
            self.mean += grade
        for grade in friend.grades:
            friend.mean += grade
        return self.mean/len(self.grades) < friend.mean/len(friend.grades)

student1 = Student("Makar",20,"Bioinformatyka")
student2 = Student("Janek",21,"Bioinformatyka")

student1.recive_grade(4)
student1.recive_grade(4)
student1.recive_grade(3)

student2.recive_grade(4)
student2.recive_grade(3)
student2.recive_grade(3)

print(student2<student1)