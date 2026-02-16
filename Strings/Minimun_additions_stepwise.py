def solution(structures):
    def get_min_additions(arr):
        n = len(arr)
        # To find the minimum additions for a stepwise pattern (arr[i] = x + i),
        # we must find the smallest starting height 'x' such that:
        # This simplifies to: x >= arr[i] - i.

        max_diff = -float('inf')
        for i in range(n):
            diff = arr[i] - i
            if diff > max_diff:
                max_diff = diff

        # max_diff is our starting 'x'. The target height for index i is max_diff + i.
        total_additions = 0
        for i in range(n):
            target_height = max_diff + i
            total_additions += (target_height - arr[i])

        return total_additions

    # For descending, we reverse the array and treat it as an ascending problem
    ascending_cost = get_min_additions(structures)
    descending_cost = get_min_additions(structures[::-1])

    return min(ascending_cost, descending_cost)
