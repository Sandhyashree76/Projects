import math
p=int(input('''Press 1: Basic calculator
Press 2: Scientific Calculator: '''))
if(p==1):
    q=int(input(''' select the operation
1- Addition
2- Subtraction
3- Multiplication
4 - Division
5 - Modules
6 - floor devision: '''))
    a=int(input('enter value 1: '))
    b= int(input('enter value 2: '))
    if(q==1):
        print(a+b)
    elif(q==2) :
        print(a-b)
    elif(q==3) :
        print(a*b)    
    elif(q==4) :
        print(a/b)
    elif q==5 :
        print(a%b)
    elif(q==6) :
        print(a//b)
if(p==2):
    
    s=int(input(''' select the trignometric fun/ other fun
1- sin
2- cos
3- tan
4 - log
5 - sqrt
6 - factorial: '''))
    d= int(input('enter value: '))
    
    if(s==1):
        print(math.sin(math.radians(d)))
    elif(s==2):
        print(math.cos(math.radians(d)))         
    elif(s==3):
        print(math.tan(math.radians(d)))
    elif(s==4):
        print(math.log(d))
    elif(s==5):
        print(math.sqrt(d))
    elif(s==6):
        print(math.factorial(d))

        
   
              
    
    
    
