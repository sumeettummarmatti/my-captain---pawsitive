list1=[]
n=int(input("enter the number of integers:" ))

for i in range(n):
    inp=int(input())
    list1.append(inp)

print(list1)

list2=[]
for i in list1:
    if i>0:
        list2.append(i)

print(list2)



