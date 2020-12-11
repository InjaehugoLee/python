# Calculator 클래스를 생성. 
# 이 클래스의 calc () 메소드는 두 수 n,m
# 'add', 'sub', 'mul', 'div' 중 하나의 문자열을 전달 받아
# 각각 n과 m의 더하기, 빼기, 곱하기, 나누기를 수행한다.
# 클래스 메소드 add(), sub(), mul(), div() 메소드를 정의
# 객체를 생성하고 cal() 메소드를 호출하면 문자열에 따라 
# 적절한 메소들르 호출하여 결과 반환

class Calculator:
    def calc(self, n, m, string):
    
        if string=='add':
            return self.__add(n,m)
        elif string=='sub':
            return self.__sub(n,m)
        elif string=='mul':
            return self.__mul(n,m)
        elif string=='div':
            return self.__div(n,m)

    def __add(self, n, m):
        return n+m

    def __sub(self, n, m):
        return n-m

    def __mul(self, n, m):
        return n*m

    def __div(self, n, m):
        return n/m

res=Calculator()
print(res.calc(3,5, 'add'))