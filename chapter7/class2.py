# Deposit 클래스 생성.
#3개의 속성 - initial, interest, n 

class Deposit:
    def __init__(self, initial, interest, n):
        self.initial=initial
        self.interest=interest
        self.n=n

    def profit(self):
        self.pro=self.initial*(1+self.interest)**self.n
        return self.pro

deposit1 = Deposit(100, 0.035,7)
deposit1.profit()
print('%d' %deposit1.pro)
        