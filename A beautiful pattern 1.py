num=int(input())
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print('-'*2,end="")
    for j in range(i):
        if(i==1):
            print(chr(96+(num-j)),end="")
        else:
            print(chr(96+(num-j)),end="-")
        
    for j in range(i,1,-1):
        if(chr(98+(num-j))==chr(96+num)):
            print(chr(98+(num-j)),end="")
        else:
            print(chr(98+(num-j)),end="-")
        
    for j in range(1,num-i+1):
        print('-'*2,end="")    
    print()
for i in range(0,num-1):
    for j in range(i+1):
        print('-'*2,end="")
    for j in range(num,(i+1),-1):
        if(i==num-2):
            print(chr(96+j),end="")
        else:
            print(chr(96+j),end="-")
    for j in range(i+2,num):
        if(chr(97+j)==chr(96+num)):
            print(chr(97+j),end="")
        else:
            print(chr(97+j),end="-")
    for j in range(i+1):
        print('-'*2,end="")
    print()
