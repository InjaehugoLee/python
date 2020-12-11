# 메소드 오버라이딩(Method Overriding)
# 자식클래스에서 부모클래스의 메소드 중 필요한 것을 수정해 다시 정의

class People:
    def __init__(self, age=0, name=None):
        self.__age=age
        self.__name=name
    def introMe(self):
        print("Name:", self.__name, "age:", str(self.__age))

class Student(People):
    def __init__(self, age=0, name=None, grade=None):
        super().__init__(age, name)
        self.__grade=grade
    def introMe(self):
        super().introMe()
        print("Grade:", self.__grade)

p1=People(29, "Lee")
p1.introMe()

s1=Student(17,"park", 2)
s1.introMe()