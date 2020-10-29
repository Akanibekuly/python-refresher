class Student: 
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
    
    def average_grade(self):
        return sum(self.grades)/len(self.grades)


student=Student("Akzhol",(100,100,93,98,90))
student2=Student("Bob",(90,90,93,78,90))
print(student.name)
print(student.grades)
print(student.average_grade())
print(student2.average_grade())