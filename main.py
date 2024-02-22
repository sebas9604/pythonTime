k = [[5,6,7],[3,4,3]]

for x in k:
    total = 0
    for y in x:
        total = total + y
    print(total)    

"""


lockers = x.split(',')
totals = set()
for x in lockers:
    total = 0
    for y in x:
        total = total + int(y)
    totals.add(total)
print(max(totals))"""

s = "cb"
k = ["cd", "bd", "cccb", "bcc", "bcdcb"]

correct_words = set()
for x in k:
    flag = 1
    for y in x:
        if (y in s):
            pass
        else:
            flag = 0
    if flag == 1:
        correct_words.add(x)
print(len(correct_words))
