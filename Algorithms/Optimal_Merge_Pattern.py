n = int(input())                 # number of rocks
rocks = list(map(int, input().split()))

total = 0

while len(rocks) > 1:            # until one rock remains
    rocks.sort()                 # sort the rocks
    a = rocks.pop(0)             # smallest rock
    b = rocks.pop(0)             # second smallest
    s = a + b
    total += s                   # add effort
    rocks.append(s)              # put new rock back

total += rocks[0]                # destroy final rock
print(total)
