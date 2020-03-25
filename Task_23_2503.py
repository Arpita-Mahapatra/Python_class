'''a=input()  #task for printing the first and thelast letter of both the string and concatenating it
b=input()
print(a+b)
print(len(a+b))
c=len(a)
d=len(b)
print(a[0::c-1]+b[0::d-1])
print(b)'''

'''a=input()
b=a[0].upper()+a[1:-1].lower()+a[-1].upper() #convert the first letter to upper case(a[0].upper())concatenate with the other letters which needs to be in lower(a[1:-1].lower()) and convert the last character into uppar case.
print(b)'''

'''a=input()  #task to conver second and second last to captial letter.
c=len(a)
b=a[0].lower()+a[1].upper()+a[2:c-3].lower()+a[c-2].upper()+a[-1].lower()
print(b)'''




'''a=input()  #task to convert second and second last to captial letter.
c=len(a)
b=a[0].lower()+a[1].upper()+a[2:c-3].lower()+a[c-2].upper()+a[-1].lower()
print(b)'''

'''a=input()  #task to convert first, last and middle character to captial letter.
c=len(a)
n=int(c/2)
b=a[0].upper()+a[1:n].lower()+a[n].upper()+a[(n+1):(c-1)].lower()+a[-1].upper()
print(b)'''

a=input()  #task to convert first letter and last letter into caps for both the strings and concatenating it.
c=len(a)
b=input()
d=len(b)
s=a[0].upper()+a[1:c-1].lower()+a[-1].upper()
t=b[0].upper()+b[1:d-1].lower()+b[-1].upper()
print(s+t)



