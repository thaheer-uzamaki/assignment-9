lst = []
n=int(input("Enter the length of the list: - "))
for i in range(n):
    lst.append(int(input()))

unique_list = [] 
for x in lst:
    if x not in unique_list:
        unique_list.append(x)
print (unique_list) 