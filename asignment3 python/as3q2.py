str="Computer Education"
res = ""
print("Original String :",str) 
for i in range(len(str)):
	if i % 2 == 0:
	  res = res + str[i]
print("Remove Odd Index Char :",res)