lists=[3,2,32,4,5,15,6]
count=len(lists)
for i in range(1,count):
    key=lists[i]
    j=i-1
    while j>=0:
        if lists[j]>key:
            lists[j+1]=lists[j]
            lists[j]=key
        j-=1
print(lists)
