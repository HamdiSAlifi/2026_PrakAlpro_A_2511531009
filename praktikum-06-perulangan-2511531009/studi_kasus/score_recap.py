PASS_SCORE = 60
EXCELLENT_SCORE = 85

scores = list()

while True:
    count = int(input())
    if count > 0:
        break
    print("Invalid student count!")

for i in range(count):
    while True:
        score = int(input())
        if 0 <= score <= 100:
            break
        print("Invalid score!")
    scores.append(score)

sum_scores = 0
for score in scores:
    sum_scores += score

average = round(sum_scores / len(scores), 2)
passed = 0
for score in scores:
    if score >= PASS_SCORE:
        passed += 1

highest = max(scores)

print("Total score: " + str(sum_scores))
print("Average score: " + str(average))
print("Passed: " + str(passed))
print("Highest score: " + str(highest))