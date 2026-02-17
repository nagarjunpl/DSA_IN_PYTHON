def first_last_sum(nums):
    s = 0
    
    for num in nums:
        s += num
    
    s = str(s)   
    
    if len(s) >= 2:
        return int(s[0]) + int(s[-1])
    else:
        return int(s)
        
print(first_last_sum([1,2,3,4,5]))   # 6
print(first_last_sum([10,20,30]))    # 6
print(first_last_sum([5]))           # 5
