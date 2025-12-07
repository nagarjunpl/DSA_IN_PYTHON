class Solution:
    def secondLargestElement(self, nums):
        if len(nums) < 2:
            print(-1)
            return

        largest = None
        second_largest = None

        for x in nums:
            if largest is None or x > largest:
                second_largest = largest
                largest = x
            elif x != largest and (second_largest is None or x > second_largest):
                second_largest = x

        if second_largest is None:
            print(-1)
        else:
            print(second_largest)
        
