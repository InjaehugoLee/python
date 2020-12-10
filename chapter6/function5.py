# 1. 지역변수
# def func1():
#     v=10
#     print("func1()의 v=%d" %v)

# def func2():
#     v=20
#     print("func2()의 v=%d" %v)

# func1()
# func2()

# 2. 전역변수
# def func1():
#     v=10
#     print("func1()의 v=%d" %v)

# def func2():
#     print("func2()의 v=%d" %v)

# v=20
# func1()
# func2()

# 3.
def func1():
    v=10
    print("func1()의 v=%d" %v)

def func2():
    #global v
    v=30
    print("func2()의 변경된 전역 v= %d" %v)

v=20

func1()
func2()
print(v)