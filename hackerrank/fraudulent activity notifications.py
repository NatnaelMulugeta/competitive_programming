def activityNotifications(expenditure, d):
    notf = 0
    isEven = False
    if d % 2 == 0:
        isEven = True
    count_lst = [0] * 201
    for i in expenditure[:d]:
        count_lst[i] += 1
    for i, j in enumerate(expenditure[d:]):
        median = getMedian(count_lst, d, isEven)
        if j >= median:
            notf += 1
        count_lst[j] += 1
        count_lst[expenditure[i]] -= 1
    return notf

def getMedian(count_lst, d, isEven):
    total = 0
    days = []
    for i, j in enumerate(count_lst):
        total += j
        if not days and d//2 <= total:
            days.append(i)
        if d//2 + 1 <= total:
            days.append(i)
            break
    if isEven:
        return sum(days)
    else:
        return days[-1] * 2

print(activityNotifications([1, 2, 3, 4, 5], 4))