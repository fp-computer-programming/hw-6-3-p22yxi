# Author Yongdong Xi
lst0 = input("Give me some numbers")
lst = lst0.split()
for i in range(len(lst)):
    lst[i] = int(lst[i])
print("Sum = ", sum(lst))
