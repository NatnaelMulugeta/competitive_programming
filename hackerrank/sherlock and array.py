def balancedSums(arr):
    left = 0
    right = len(arr) - 1
     
    left_sum = arr[left]
    right_sum = arr[right]
     
    while left != right:
        if left_sum < right_sum:
            left += 1
            left_sum += arr[left]
        else:
            right -= 1
            right_sum += arr[right]
     
    if right_sum == left_sum:
        return "YES"

    return "NO"