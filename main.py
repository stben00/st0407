 
 
 
 
 
def calculator():
    
    
    print("the simple calculator")
    print(" Available operations: +, -, *, /")

    try: 
        num1 = float(input("Enter first number: "))
        operator = input("Enter operations:  +, -, *, /")
        num2 = float(input("Eenter a second number:  "))
        



        if operator == "+":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif operator == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        
        elif operator == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif operator == "/":
            if num2 == 0:
                print("Division by zero in not allowed ! ")
                return 
            result = num1 / num2
        
        
        else:
            print("Error: Invalid operator ! ")
            return 
        
        
        print(f"Final Result: {result}")
    
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")


calculator()
 






 

import random

print("Добро пожаловать в игру 'Разминка для Мозга ' !")
print("Твоя задача сладывать правильно числа. Поехали!\n ")

score = 0

for i in range(5):
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    
    print(f"Пример {i + 1}: {a} + {b} = ?")
    user_answer = int(input("Ваш ответ: "))
    
    
    correct_answer = a + b
    
    if user_answer == correct_answer:
        print("Правильный ответ !\n")
        score += 1
    
    else: 
        print("Ответ неверный !")
        print("Правильный результат: ", correct_answer, "\n")
print(f"Игра окончена!. Ты набрал {score} из 5 баллов. ")
    
    
    

secret_password = 123
max_attempts = 3
attempts = 0
success  = False

while attempts < max_attempts:
    try:
        password = int(input("Enter your password: "))
        
        if password == secret_password:
            print("Welcome")
            success = True
            break
        else:
          attempts += 1
          print(f"Error: Invalid password. Attempts left : {max_attempts - attempts}")
            
    except ValueError:
        attempts += 1
        print(f"Use only numbers. Attempts left: {max_attempts - attempts}")
        
if not success:
    print("You habe used all attempts. Access denied")



    

    
    
    