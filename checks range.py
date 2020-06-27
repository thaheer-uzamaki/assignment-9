def check(s,e,c):
    for i in range(s,e+1):
        if i==c:
            print("The number is present in the range")
            break
start=int(input("Enter a number for starting range: - "))
end=int(input("Enter a number for ending range: - "))
chk=int(input("Enter a number for checking: - "))
check(start,end,chk)