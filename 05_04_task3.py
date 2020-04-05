tuple1=(1,4,5,6,7)
tuple2=(5,6,7,8,9)
x=list(set(tuple1)) #remove duplicates
y=list(set(tuple2))
list3=x+y #concatenate two tuples after duplicate removal from both
tuple3=tuple(list3) #o/p:(1, 4, 5, 6, 7, 5, 6, 7, 8, 9)
print(tuple3)
print(tuple3.index(9)) #find the index value of 9 #o/p:9
tuple4=(0,4,5)
set1=set(tuple3)
set2=set(tuple4)
r=set1.intersection(set2) #find common elements between above elements with {0,4,5}
tuple5=tuple(r)
print(tuple5) #o/p:(4, 5)
mul=tuple4*3 #multiple above tuple 3 times
print(mul)#o/p:(0, 4, 5, 0, 4, 5, 0, 4, 5)




