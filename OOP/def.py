class Student():
    def __init__(self,fullname):
        self.name=fullname
        print("Adding new constructor to database")

s1 = Student("Tufail")
print(s1.fullname)        