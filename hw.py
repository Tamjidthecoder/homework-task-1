print("Full pyramid pattern of triangle(^:) ")
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i + 1):
        print("^ ", end="")
    print()
for i in range(n-1,0,-1):
    for j in range(i + 1):5
        print("^ ", end="")
    print()