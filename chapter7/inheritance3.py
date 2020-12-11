class People :
    def setData(self, age, name):
        self.__age=age
        self.__name=name

    def introMe(self):
        print("Name :", self.__name, "age :", str(self.__age))

class Teacher(People) :
    def __init__(self, school=None) :
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)

t1 = Teacher("HighSchool")
t1.setData(48, "Kim")
t1.introMe()
t1.showSchool()