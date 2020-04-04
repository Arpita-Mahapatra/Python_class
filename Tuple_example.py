'''tuple1=("hello",) #concatenating tuple
tuple2=("Welcome","to","class")
tuple3=tuple1+tuple2
print(tuple3)''' #output: "hello","Welcome","to","class"



'''tuple1=(1,2,4,5) #multiplication of tuple
tuple3=tuple1*3
print(tuple3)''' #output: (1,2,4,5,1,2,4,5,1,2,4,5)



'''tuple1=(1,4,5,6,5,7,5,6) #count() function
x=tuple1.count(5)
print(x)''' #output: 3


'''tuple1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5) #index function

x = tuple1.index(8)

print(x)''' #output: 3


tuple2= (1,5,6,4,8) #converting tuple to list
x=list(tuple2)
print(x) #output:[1, 5, 6, 4, 8]
x[2][5][3]=45,67,56
print(x) #[1, 5, 45, 4, 8]
tuple3=tuple(x) #converting list back to tuple
print(tuple3)
