n = int(input())  # 4
rocks = list(map(int, input().split())) # 4 3 2 6

total = 0

while len(rocks) > 1:
    rocks.sort()          # sort the list

    a = rocks.pop(0)      # smallest
    b = rocks.pop(0)      # second smallest

    s = a + b             # merge cost
    total += s
    rocks.append(s)       # add back

# add last remaining rock
total += rocks[0]
print(total) # Output : 44

