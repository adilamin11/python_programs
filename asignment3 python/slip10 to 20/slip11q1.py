n = int(input("enter the number"))
sum =0
rem =0
for i in range(0,n+0):
    rem = n %10
    sum = sum + rem
    n = n//10
print("sum of digit is ",sum)