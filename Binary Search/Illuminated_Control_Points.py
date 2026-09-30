def solution(lamps, points):
    result = []
    for p in points:
        count = 0
        for start, end in lamps:
            if start <= p <= end:
                count += 1
        result.append(count)
      
    return result

# Test with the example 
lamps = [[1, 7], [5, 11], [7, 9]]
points = [7, 1, 5, 10, 9, 15]

print(solution(lamps, points))
# Output: [3, 1, 2, 1, 2, 0]
