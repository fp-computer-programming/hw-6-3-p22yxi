# Question 2

numblst = input("Give me a list of numbers")
numblst1 = numblst.split()
numblst2 = numblst.split()
print(type(numblst1))
print(numblst1)
numblst1.sort()
print(numblst1)
if numblst1 == numblst2:
    print("Those numbers are sorted")
