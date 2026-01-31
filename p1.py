# Sum of digits of a number

import time 

def sum_of_digits1(number):
    s = 0
    for n in str(number):
        s+=int(n)
    return s 

# more faster
def sum_of_digits2(number: int) -> int:
    return sum(map(int, str(number)))


# math version 
def sum_of_digits3(number: int) -> int:
    number = abs(number)
    s = 0
    while number:
        s += number % 10
        number //= 10
    return s

number = int(input("enter number: "))
t1 = time.time()
s = sum_of_digits3(number)
t2 = time.time()
print("sum: ", s, t2-t1)
        