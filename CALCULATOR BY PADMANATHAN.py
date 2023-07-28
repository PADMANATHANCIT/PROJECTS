def ADDITION(x,y):
    result=x+y
    return result
def SUBTRACTION(x,y):
    result=x-y
    return result
def MULTIPLICATION(x,y):
    result=x*y
    return result
def DIVISON(x,y):
    result=x/y
    return result
def MODULUS(x,y):
    result=x%y
    return result
while True:
    number1=int(input("Enter Your First Number:"))
    number2=int(input("Enter Your Second Number:"))
    print('''
             CHOICE 1-------TO PERFORM ADDITION
             CHOICE 2-------TO PERFORM SUBTRACTION
             CHOICE 3-------TO PERFORM MULTIPLICATION
             CHOICE 4-------TO PERFORM DIVISON
             CHOICE 5-------TO PERFORM MODULUS
''')
    choice=int(input("Enter Your Desired Choice:"))
    calculator=[ADDITION,SUBTRACTION,MULTIPLICATION,DIVISON,MODULUS]
    RESULT=calculator[choice-1](number1,number2)
    print("THE OUTPUT OF YOUR DESIRED ARITHMETIC OPERATION IS",RESULT)
    exitchoice=input("Enter Q Or q to exit:")
    if exitchoice=='Q' or exitchoice=='q':
        break
        
   
              
