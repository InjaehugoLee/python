# # enumerate
# names=['Corey', 'Chris', 'Dave', 'Travis', 'Smith']
# for index, name in enumerate(names, start=1):
#     print(index, name)

# map

# def Squares(n):
#     return n**2
# numbers=[1,3,5,9]   

# print(list(map(Squares, numbers))) # list로 묶어줘야 함

# zip 

names= ['Peter parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')