class Solution:
    def duplicateZeros(self, arr):
        n = len(arr)
        i = 0
        while i < n:
            if arr[i] == 0:
                arr.insert(i + 1, 0)
                i += 1
                arr.pop()
            i += 1
        print("After duplicating zeros:", arr)

a = Solution()
user_input = input("Enter numbers like [1,0,2,3,0,4,5,0]: ")

# Clean input with brackets and commas
user_input = user_input.strip().strip('[]')
arr = list(map(int, user_input.split(',')))

a.duplicateZeros(arr)
