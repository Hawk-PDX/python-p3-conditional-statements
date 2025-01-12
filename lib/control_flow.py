#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'admin' or username == 'ADMIN') and password == '12345':
        return "Access granted"
    else:
        return "Access denied"
       
print(admin_login('sudo', '12345'))

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        temperature > 65 and temperature < 85
        return "It's perfect out there!"

hows_the_weather(33)
hows_the_weather(99)
hows_the_weather(75)
            
def fizzbuzz(num):
    if num % 3 == 0 and (num != 15 and num != 45 and num != 0): 
        return "Fizz"
    elif num % 5 == 0 and (num != 15 and num != 45 and num != 0):
        return "Buzz"
    elif num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    else:
        return num

print(fizzbuzz(0))
print(fizzbuzz(1))
print(fizzbuzz(2))
print(fizzbuzz(3))
print(fizzbuzz(4))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(45))


def calculator(operation, num1, num2):
    # your code here
    pass


