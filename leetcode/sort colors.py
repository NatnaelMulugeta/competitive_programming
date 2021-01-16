def sortColors(nums):
    r, w, b = 0, 0, len(nums)-1

    while w <= b:
        idx = nums[w]
        if idx == 0:
            nums[w] = nums[r]
            nums[r] = 0
            r += 1
            w += 1
        elif idx == 1:
            w += 1
        elif idx == 2:
            nums[w] = nums[b]
            nums[b] = 2
            b -= 1
    print(nums)
    '''

    n = len(nums)
    for i in range(0, n):
        if nums[i] == 0:
            nums[w] = nums[r]
            nums[r] = 0
            r += 1
            w += 1
        elif nums[i] == 1:
            w += 1
        elif nums[i] == 2:
            nums[w] = nums[b]
            nums[b] = 2
            b -= 1
    print(nums)



sortColors([1,0,0,2,1,0,1])