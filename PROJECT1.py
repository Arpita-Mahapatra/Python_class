#Ds/Dt Calculator
#Algebra Functions

Functions={1:"Numbers",2:"List",3:"Sets",4:"Strings",5:"Tuples",6:"Dictionaries"}
for values,keys in Functions.items():
    print(values,keys) #to print all the keys with their values.
Func_input=int(input("Enter the function to be performed from above options:"))

    

def Number_Operations():
    Number_ops={1:"Add",2:"Subtract",3:"Multiply",4:"Divide",5:"Floor Division",6:"Power",7:"Mod",8:"Square",9:"Square root",10:"Cube",11:"Cube root",12:"Prime",13:"Armstrong",14:"Fibonacci",15:"Factorial",16:"Odd/ Even"}
    for values,keys in Number_ops.items():
        print(values,keys)

    Num_Func=int(input("Enter the Algebra function to be performed from above options:"))
    x, y = map(int, input("Enter two numbers seperated by ',':").split(","))
         #print(x,y)
    import math
    if Num_Func==1: #if user chose 1 then we need to perform addition
             sum1=x+y
             print("The sum of numbers is:", sum1)

    elif Num_Func==2:
             sub=x-y
             print("The difference between the number is:",sub)

    elif Num_Func==3:
             prod=x*y
             print("The product of the numbers is:",prod)

    elif Num_Func==4:
             div=x/y
             print("The division value of the numbers is:",div)

    elif Num_Func==5:
             print("The floor division value is:", math.floor(x//y))

    elif Num_Func==6:
             print("The power value is:", math.pow(x,y))

    elif Num_Func==7:
             print("The Mod of numbers is:", math.fmod(x,y))

    elif Num_Func==8:
             print("The square of x is:",(x**2))

    elif Num_Func==9:
             print("The square root of x is:", math.sqrt(x))
             
             
    elif Num_Func==10:
             print("The cube of x is:",(x**3))

    elif Num_Func==11:
             print("The cube root of x is:",(x**(1/3)))

         
    elif Num_Func==12:
             for val in range(x, y+1): 
                    if val > 1: 
                        for n in range(2, val//2 + 2): 
                            if (val % n) == 0: 
                                break
                            else: 
                                if n == val//2 + 1: 
                                    print("The Prime numbers between x and y are:", val)

            


    elif Num_Func==13:

             for num in range(x,y+1):
               # initialize sum
                sum = 0
 
                # find the sum of the cube of each digit
                temp = num
                while temp > 0:
                   digit = temp % 10
                   sum += digit ** 3
                   temp //= 10
 
                if num == sum:
                   print(num)

    elif Num_Func==14:
                def Fibonacci(n): 
                    if n<0: 
                        print("Incorrect input") 
                    # First Fibonacci number is 0 
                    elif n==1: 
                        return 0
                    # Second Fibonacci number is 1 
                    elif n==2: 
                        return 1
                    else: 
                        return Fibonacci(n-1)+Fibonacci(n-2) 
  
                    # Driver Program 
  
                print("The fibonacci of x is:",Fibonacci(x))
                print("The fibonacci of y is:",Fibonacci(y))

    elif Num_Func==15:
                print("The factorial of x is:",math.factorial(x))
                print("The factorial of y is:",math.factorial(y))


    elif Num_Func==16:
            if (x%2)==0:
                print("Number given is an even number")

            else:
                print("Number given is an odd number")
if Func_input==1:
    Number_Operations()



    def List_Operations():

        List_ops={1:"Create List",2:"Length of List",3:"Min",4:"Max",5:"Add",6:"Insert",7:"Sort",8:"Remove",9:"Pop",10:"Concate",11:"Slicing/indexing",12:"Replace",13:"Duplicates"}

        for values,keys in List_ops.items():
             print(values,keys)




if Func_input==2:
    List_Operations()






















