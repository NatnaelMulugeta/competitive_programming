def intersection(nums1, nums2):
    nums1 = list(dict.fromkeys(nums1))
    nums2 = list(dict.fromkeys(nums2))

    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1

    result = []
    for i in nums1:
        if i in nums2:
            result.append(i)

    return result

print(intersection([1,2.1,1,8,5], [3,1,8,6,6]))