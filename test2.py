# n = int(input('enter a number:'))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# total = 0
# for i in range(1, 101):
    # total += i
# print(total)

# numbers = [5, 20, 3, 8, 15]
# biggest = numbers[0]
# for n in numbers:
#     if n > biggest:
#         biggest = n
# print(biggest)

# import random


# robtiv = random.randint(1, 10)
# tiv = int(input('enter a number:'))
# while tiv != robtiv:
#     if tiv < robtiv:
#         print("the number is less than the random number")
#     elif tiv > robtiv:
#         print("the number is greater than the random number")
#     tiv = int(input('enter a number:'))
# print("you guessed the number correctly!")



def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(int(input('enter a number:'))))    