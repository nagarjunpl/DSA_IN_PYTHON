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
