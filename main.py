 
 
 
 
 
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
 

