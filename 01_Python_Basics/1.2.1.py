n = int(input())
marks = list(map(int, input().split()))

fail = False

for m in marks:
    if m < 40:
        fail = True
        break

if fail:
    print("Fail")
else:
    avg = sum(marks) / n
    print("Aggregate Percentage: {:.2f}".format(avg))

    if avg > 75:
        print("Grade: Distinction")
    elif avg >= 60:
        print("Grade: First Division")
    elif avg >= 50:
        print("Grade: Second Division")
    else:
        print("Grade: Third Division")
