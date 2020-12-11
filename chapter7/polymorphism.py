# 다형성 (polymorphism)
# 전달된 인자에 따라 함수 또는 연산의 기능이 달라지는 기능

class Korean(object):
    def greeting(self):
        print("안녕하세요")

class American(object):
    def greeting(self):
        print("Hello")

def sayhello(people):
    people.greeting()

Kim = Korean()
John = American()
sayhello(Kim)
sayhello(John)