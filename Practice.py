# adding two list and remove common elements

l1 = [1,2,3,4,5,6]
l2 = [2,5,7,8,9,10]

for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)    