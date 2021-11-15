# Author Yongdong Xi (Nov 15)

# Question 1
ques = input('Give me a word')
ansr = input('Give me another one')
lst1 = list(ques)
lst2 = list(ansr)
lst1.sort()
lst2.sort()
if lst1 == lst2:
    print('the words are anagrams')


