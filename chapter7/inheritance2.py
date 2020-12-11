# 예제의 Teacher 클래스에서 People 클래싀으 __init__()를 호출하지 않고
# 부모 클래스의 age, name 속성을 이용할 수 있는가?
# 이용할 수 없다면 그 이유는?
# 이용할 수 있게 하려면 어떻게 수정? (캡슐화 개념)

class People :
    def __init__(self, age=0, name=None):
        self.age = age
        self.name = name

    def introMe(self):
        print("Name :", self.name, "age :", str(self.age))

class Teacher(People) :
    def __init__(self, school=None) :
        self.school = school

    def showSchool(self):
        print("My School is ", self.school)

t1 = Teacher("HighSchool")
t1.age=48
t1.name="Kim"
t1.introMe()
t1.showSchool()

