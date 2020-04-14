#palindrome or not
'''def palindrome(x):
    sum1=0 #initialized sum1 to 0 so that we do not get blank value in later use
    num=x #assigned num with x because x value will keep changing while iteration in while loop
    while(num!=0): #to check whether num value is not 0
        rem=int(num%10) 
        sum1=int(sum1*10+rem)#1st iteration value 2nd iteration value 42 3rd iteration value 424
        num=int(num/10)
        #print(sum1)
        #print(num)
        
    
    if(sum1==x):
        print("number is palindrome")

    else:
        print("number is not a palindrome")

        

palindrome(424)''' #o/p: number is palindrome


# write function to check whether a no is odd or even

'''def odd_even(num):
    if (num%2)==0: #if the number is divisible by 2 then even  number else odd number
        print("even number")

    else:
        print("odd number")

odd_even(45)''' #o/p: odd number

# write a function to check whether a string is palindrome

'''def Str_palindrome(x):
    
    revx=x[::-1] #will print the string in reverse
    if x==revx: #if the string 'x' is equal to reverse string 'revx' then it is palindrome
        print("string is a palindrome")

    else:
        print("string is not a palindrome")

Str_palindrome("malayalam")''' #o/p:string is a palindrome

# write function to check whether a no is +ve or -ve
'''def Pos_neg(x):
    if(x>0):
        print("number is positive")

    else:
        print("number is negetive")


Pos_neg(-9)''' #o/p:number is negetive

# get two numbers from user and do below process (a + b)(a - b)

'''def Mult(x,y):
    prod=(x+y)*(x-y)
    print(prod)


a=int(input())
b=int(input())
Mult(a,b)''' #o/p:44

# get three numbers from user and do below process(a + b)(a - b)(a-c)
'''def Mult(x,y,z):
    prod=(x+y)*(x-y)*(x-z)
    print("The resilt is", prod)


a=int(input())
b=int(input())
c=int(input())
Mult(a,b,c)''' #o/p:The resilt is 132
