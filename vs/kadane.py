a = list(map(int, input().split()))
first= 0
last = len(a) - 1
curr = 0
maxtillnow = 0
for x in a:
    curr += x
    if maxtillnow <= curr:
        maxtillnow = curr
    elif maxtillnow > curr:
        curr = 0
print(maxtillnow)