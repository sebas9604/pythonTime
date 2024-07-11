"""k = [[5,6,7],[3,4,3]]

for x in k:
    total = 0
    for y in x:
        total = total + y
    print(total)    

"""

""""
lockers = x.split(',')
totals = set()
for x in lockers:
    total = 0
    for y in x:
        total = total + int(y)
    totals.add(total)
print(max(totals))"""
"""""
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
"""

"""contacts =[
    ('James',42),
    ('Amy',24)
]

name = 'James'
for x in contacts:
    if name == x[0]:
        print(name)
"""
"""
def convert(num):
    if num == 1:
        return 1
    return (num % 2 + 10 * convert(num//2))

print(convert(0))"""

def cal_segundo(n, arr):
    for x in arr:
        for y in arr:
            if x > y and x < mayor:
                segundo = x
            else:
                break
    return segundo



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mayor = max(arr)
    arr = list(arr)
    print(cal_segundo(n, arr))

    
                            