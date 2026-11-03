height = int(input("Enter heights: "))

for row in range((height + 1), 0, -1):
    for column in range (row):
        print("*", end=" ")
    print()