dict1={1:["english","maths","science"],2:(10,20,40,"python program"),3:["bio-zoology","bio-botany","physics"]} #create a dictionary {1:["english","maths","science":["bio-zoology","bio-botany","physics"]],2:(10,20,40,"python program")}
print(dict1)
print(dict1[3][1][4:])#extract botany
x=dict1.get(1)
print(x) #o/p:['english', 'maths', 'science']
tuple1=tuple(x)
print(tuple1) #o/p:('english', 'maths', 'science')
print(len(tuple1))#o/p:3
print(dict1.keys()) #dict_keys([1, 2, 3])






