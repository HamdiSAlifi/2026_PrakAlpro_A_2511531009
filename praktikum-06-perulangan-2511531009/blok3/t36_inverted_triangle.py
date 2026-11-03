height = int(input("Enter heights: "))

for row in range(1, (height + 1)):
    for column in range (height,  0 , -1):
        print("*", end=" ")
    print()