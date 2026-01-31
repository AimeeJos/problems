# Reverse a number without string conversion

def reverse_number1(number):
    new_no=[]
    for i in range(len(str(number))):
        digit = number%10
        number = number//10
        new_no.append(str(digit))
    reversed_no = "".join(new_no)
    return reversed_no 

def reverse_number2(number: int) -> int:
    reversed_no = 0
    number = abs(number)

    while number > 0:
        reversed_no = reversed_no * 10 + number % 10
        number //= 10

    return reversed_no   
        
reversed_no = reverse_number2(123)
print(reversed_no)