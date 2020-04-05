list1=[]
list2=[5,6,8,9]
list3=list1+list2 #concatenate with [5,6,8,9]
print(list3)
list3.extend([8,9,1,5,6,7,8])#add 8,9,1,5,6,7,8
print(list3)
x=list3.count(8)#count of 8
print(x)
avg=sum(list3)/len(list3)#avg
print(avg)
cal=sum(list3)+min(list3)+max(list3)#sum of list+min+max
print(cal)
mean=sum(list3)/len(list3)#mean
print(mean)
list3.sort()
l=int(len(list3)/2)
median=list3[l]
print(median)
list4=list(set(list3))
print(list4)
tuple1=tuple(list4)
print(tuple1)
