set1=set()
set2=set()
set1.update([7,8,9,1,2,3,4,5,0]) #update set1 with 7,8,9,1,2,3,4,5,0
set2.update([4,5,6,0])#update set2 with 4,5,6,0
print(set1) #o/p:{0, 1, 2, 3, 4, 5, 7, 8, 9}
print(set2) #o/p:{0, 4, 5, 6}
x=set2.issubset(set1)#check whether set2 is subset of set 1 ?
print(x) #o/p:False
y=set1.isdisjoint(set2)#check whether both are disjoint ?
print(y)#o/p:False
set1.remove(8)#remove 8 from set1
print(set1)#o/p:{0, 1, 2, 3, 4, 5, 7, 9}
set2.discard(0)#discard 0 from set2
print(set2)#o/p:{4, 5, 6}
unu=set1.union(set2)#find sum(set1 union set2)
sum1=sum(unu)
print(sum1)#o/p:37





