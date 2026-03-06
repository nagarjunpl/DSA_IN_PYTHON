def solution(diffs):
    current_rating = 1500
    highest_rating = 1500
    
    for change in diffs:
        # Update the current rating
        current_rating += change
        
        # Check if the new current rating is the highest we've seen
        if current_rating > highest_rating:
            highest_rating = current_rating
            
    return [highest_rating, current_rating]
    
diffs = [100, -200, 300, -50]
print(solution(diffs))  # Output: [1700, 1650]

# Step by step:
# Start rating = 1500
# 1500 + 100 = 1600  (highest = 1600)
# 1600 - 200 = 1400
# 1400 + 300 = 1700  (highest = 1700)
# 1700 - 50 = 1650
