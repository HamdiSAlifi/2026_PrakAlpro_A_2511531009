seats = int(input())

for row in range(1, 4):
    print("Row " + str(row) + ":", end="")
    for seat in range(1, 6):
        if seat >= seats:
            break
        print(" " + str(seat), end="")
    print()