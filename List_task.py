'''a=[2,5,4,8,9,3] #reversing list
a.reverse()
print(a)''' #[3, 9, 8, 4, 5, 2]

'''a=[1,3,5,7,9] #deleting element from list
del a[1]
print(a)''' #[1, 5, 7, 9]

'''a=[6,0,4,1] #clearing all elements from list
a.clear()
print(a)''' #o/p : []

'''n = [1, 2, 3, 4, 5] #mean
l = len(n) 
nsum = sum(n) 
mean = nsum / l
print("mean is",mean)''' #o/p: mean is 3.0

'''n=[6,9,4,3,1] #median
n.sort()
l=int(len(n)/2)
median=n[l]
print(median)''' #O/P : 4

'''n=[2,6,4,9,3] #avg of first, middle,last elements
l=int(len(n)/2)
avg= (n[0]+n[l]+n[-1])/3
print(avg)''' #O/P : 3.0

'''a=[[1,2,3],4,5,6,[8,9],[[44,55,66],[66,77],["Hello","Python","Welcome"]]]
print(a[5][2][2][3:])''' #print "come"

  
'''a=[[1,2,3],4,5,6,[8,9],[[44,55,66],[66,77],["Hello","Python","Welcome"]]]
print(a[5][2][2])''' #o/p: Welcome

'''a=[[1,2,3],4,5,6,[8,9],[[44,55,66],[66,77],["Hello","Python","Welcome"]]]
print(a[5][2][1][1:4])''' #o/p:yth

a=[[1,2,3],4,5,6,[8,9],[[44,55,66],[66,77],["Hello","Python","Welcome"]]]
print(a[5][2][1:]) #o/p:['Python', 'Welcome']
