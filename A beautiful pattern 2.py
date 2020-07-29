n=int(input())
for j in range(n,-1,-1):
	print(' '*(n-j)*2,end='')
	for i in range(j,-1,-1):
		print(i,end=" ")
	for i in range(1,j+1):
		print(i,end=" ")
	print()
for j in range(n,0,-1):
	print(' '*(j-1)*2,end='')
	for i in range((n-j)+1,-1,-1):
		print(i,end=" ")
	for i in range(1,(n-j)+2):
		print(i,end=" ")
	print()
