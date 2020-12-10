# def prtMesg(message, count=1):
#     print(message * count)
# prtMesg('default')
# prtMesg('Hi!', 5)

# def greet(name, msg="Nothing new?"):
#     print("Hi!", name + ',' +msg)
# greet("Abe")
# greet("Bob", "Good morning!")

# def total(*numbers):
#     sum=0
#     for n in numbers:
#         sum+= n
#     return sum
# print(total(1,2,3))
# print(total(1,2,3,4,5))

# def dicPresident(**keywords):
#     for i in keywords.keys():
#         print("%s : %d-th president" %(i, keywords[i]))

# dicPresident(Kennedy = 35, Obama = 44, Trump=45)

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
