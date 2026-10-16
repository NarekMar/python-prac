# name = input('enter a name:')
# qanak = 0
# for i in name.lower():
#     if i == 'a':
#         qanak += 1
# print(qanak)         

# def average(numbers):
#     if len(numbers) == 0:
#         return 0
#     return sum(numbers) / len(numbers)

# number = input('enter a number:')
# numbers = [int(x) for x in number.split()]

# print(average(numbers))


# friends = {"Анна": 20, "Ашот": 22, "Лена": 19}

# for name, age in friends.items():
#     print(f'{name} is {age} years old.')

# with open('notes.txt', "w", encoding="utf-8" ) as f:
#     f.write("arajin text\n")
#     f.write("erkrodrd text\n")
#     f.write("errord text\n")

# with open('notes.txt', 'r', encoding = "utf-8") as f:
#     text = f.read()   
#     print(text)


# while True:
#     try:
#         arajin = int(input('gri araji tivy:'))
#         erkrord = int(input('gri erkrord tivy:'))
#         break        
#     except ValueError:
#         print('invalid input')

# gorcoxutyun = input('gri gorcoxutyuny:')

# if gorcoxutyun == '+':
#     print(arajin + erkrord)
# elif gorcoxutyun == '-':
#     print(arajin-erkrord)
# elif gorcoxutyun == '*':
#     print(arajin*erkrord)
# elif gorcoxutyun == '/':  
#     try:
#         print(arajin/erkrord)
#     except ZeroDivisionError:
#         print('division by zero is not allowed')
# else:
#     print('unknown operation')


# try except fileri het ete chlini error tal 

try:
    with open ('notes.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()
        print(text)
except FileNotFoundError:
    print('file not found')