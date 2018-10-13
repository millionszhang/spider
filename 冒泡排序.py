numbers=[2,21,13,6,4,12,5,14]
for i in range(len(numbers)):
    for j in range(i):
        if numbers[j]>numbers[i]:
            numbers[j],numbers[i]=numbers[i],numbers[j]
print(numbers)
