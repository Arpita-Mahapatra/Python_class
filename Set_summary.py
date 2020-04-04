#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
'''sset = {"apple", "banana", "cherry"}
print(sset)''' #o/p:{'banana', 'apple', 'cherry'}

#To add one item to a set add() used.To add more than one item to a set use the update() method.
'''tset = {"apple", "banana", "cherry"}

tset.add("orange")

print(tset)'''#o/p:{'cherry', 'banana', 'orange', 'apple'}

#update()

'''t1set = {"apple", "banana", "cherry"}

t1set.update(["orange", "mango", "grapes"]) #doubt

print(t1set)'''

#to remove item we use remove(),discard(),pop(),clear(),del()
'''set1 = {"apple", "banana", "cherry"}

set1.remove("banana")

print(set1)''' #o/p:{'cherry', 'apple'}

#discard():doesn't raise error if the item does not exist in set

'''sset = {"apple", "banana", "cherry"}

sset.discard("banana")

print(sset)''' #o/p:{'apple', 'cherry'}

#clear()
'''set1 = {"apple", "banana", "cherry"}

set1.clear()

print(set1)'''

#del()
'''set1 = {"apple", "banana", "cherry"}

del set1

print(set1)''' #o/p: set1 not defined

#joining two sets using union() and update()
'''set1 = {23,24,25}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)''' #o/p:{1, 2, 3, 23, 24, 25}

#update()
'''set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)''' #o/p:{1, 2, 3, 'c', 'b', 'a'}

#The difference() method returns a set that contains the difference between two sets.
#The returned set contains items that exist only in the first set, and not in both sets.

'''a={1,3,4,5,6,7}
b={4,5,6,7,9,10}
c=a.difference(b)
print(c)''' #o/p:{1,3}

'''a={1,3,4,5,6,7}
b={4,5,6,7,9,10}
c=b.difference(a)
print(c)''' #o/p:{9, 10}

#the difference_update() method removes the unwanted items from the original set.
'''a={1,3,4,5,6,7}
b={4,5,6,7,9,10}
b.difference_update(a)
print(b)''' #o/p:{9, 10}

#The intersection() method returns a set that contains the similarity between two or more sets.
'''x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) 
print(z)''' #o/p:{'apple'}

#The intersection_update() method removes the items that is not present in both sets (or in all sets if the comparison is done between more than two sets).
'''x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) 

print(x)''' #o/p:{'apple'}

#The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
'''x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)'''  #o/p:True

#The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
'''x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y) 

print(z)''' #o/p:True

#The symmetric_difference() method returns a set that contains all items from both set, but not the items that are present in both sets.
'''x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y) 

print(z)''' #o/p:{'google', 'microsoft', 'banana', 'cherry'}

#The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
'''x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

z = x.issuperset(y) 

print(z)''' #o/p:True
