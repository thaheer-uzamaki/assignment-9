from itertools import zip_longest

a = []
n=int(input("Enter the length of list: - "))
for i in range(n):
    a.append(int(input()))
    
res = [i for i, j in zip_longest(a, a[1:]) 
                                                if i != j] 
  
# printing result  
print ("List after removing consecutive duplicates : " +  str(res)) 