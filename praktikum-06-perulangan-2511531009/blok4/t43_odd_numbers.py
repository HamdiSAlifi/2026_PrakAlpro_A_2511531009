number = 1

while number <= 6:
    if number % 2 == 0: # iteration 2 -> 2 % 2 == 0, jalan terus
        number += 1 
        continue
    print(number)
    number += 1
        