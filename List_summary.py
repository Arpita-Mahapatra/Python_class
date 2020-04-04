#List: It is a collection of data which can be ordered and changeable. It accepts duplicates as well. Written within square brackets.
'''list1=[1,3,5,"hello"]
print(type(list1))
print(list1)'''

#accessing items in the list using indexing
'''list1=[34,89,12,54,67,9,45,23]
list2=[list1[0:2],list1[3:7:3]]
print(list2)'''

#changing item value
'''list1=["hello","Welcome","to","class"]
list1[3]="Blore"
print(list1)''' #o/p:['hello', 'Welcome', 'to', 'Blore']

#length of list
'''list2=[2,4,6,4,78,9,65,2,3]
print(len(list2))''' #o/p:9

#add item using append
'''a=["apple","orange","banana"]
a.append("mango")
print(a)''' #o/p:['apple', 'orange', 'banana', 'mango']

#add item using insert
'''a1=["apple","orange","banana"]
a1.insert(1,"melon")
print(a1)''' #o/p:['apple', 'melon', 'orange', 'banana']

#remove item using remove(),del(),clear(),pop()
'''a2=[2,6,7,9,11,19]
a2.clear()
print(a2)''' #o/p: []

'''a2=[2,6,7,9,11,19]
a2.pop()
print(a2)'''#o/p:[2,6,7,9,11]

'''a2=[2,6,7,9,11,19]
a2.remove(2)
print(a2)''' #o/p:[6, 7, 9, 11, 19]

'''a2=["cat","bat","mat","rat"]
del a2[0::2]
print(a2)''' #o/p:['bat', 'rat']

#join two list
'''list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)''' #o/p:['a', 'b', 'c', 1, 2, 3]

#Reverse the order of the list
'''a=["nut","cut","hut","put"]
a.reverse()
print(a)'''#o/p:['put', 'hut', 'cut', 'nut']

#The index() method returns the position at the first occurrence of the specified value.
'''a=["nut","cut","hut","put"]
x= a.index("cut")
print(x)''' #o/p:1

#sort() function is used to sort the elements in the list.
'''a=[1,20,8,67,9,23]
a.sort()
print(a)'''#o/p:[1, 8, 9, 20, 23, 67]

#count()views the number of times the element appears in the list
'''fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)''' #o/p:1

