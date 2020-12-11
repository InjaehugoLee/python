# 다음 Person 클래스를 상속 받는 Employee 클래스를 정의하라
# Employee 클래스에 employeeID 속성 추가
# getID() 메소드를 정의하라

# getID() 메소드는 employeeID를 반환하는 메소드이다.
# Employee 클래스를 이용하여 Employee("동양", 65, 2019)로
# 생성된 객체의 이름, 나이, ID를 출력하라.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
    def introMe(self):
        print("Name :", str(self.name), "Age :", self.age)

   
class Employee(Person):
    def __init__(self, name, age, employeeID):
        super().__init__(name, age)
        self.employeeID=employeeID
        

    def getID(self):
        super().introMe()
        print("ID :", self.employeeID)
        
p1=Employee("동양",65,2019)
p1.getID()