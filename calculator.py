# operators 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#operation sign
print("Choose operation sign: ")
print("Addition(1)")
print("Subtraction(2)")
print("Multiplication(3)")
print("Division(4)")

operator = input("Choose 1, 2, 3, or 4: ") # operation selector


while(True):

    if operator in ('1', '2', '3', '4'):
        num1 = float(input("First number: ")) # input first value
        num2= float(input("Second number: ")) # input second value
        #calculation
        if operator == '1':
            print(f'{num1} + {num2} = ', add(num1, num2))
        elif operator == '2':
            print(f'{num1} - {num2} = ', subtract(num1, num2))
        elif operator == '3':
            print(f'{num1} * {num2} = ', multiply(num1, num2))
        elif operator == '4':
            print(f'{num1} + {num2} = ', divide(num1, num2))
    else:
        print("Invalid number.")
    
    
    # Asking user if they want to continue using this application
    userDecides= input("Do you want to continue [y/n]?: ") 
    if userDecides == 'n':
        print("Come back if you want to.")
        break
