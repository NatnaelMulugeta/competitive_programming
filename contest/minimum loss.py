def minimumLoss(price):
    p_lst = list(enumerate(price))
    p_lst.sort(key = lambda i: i[1])

    for i in p_lst:
        i = list(i)
    
    min_loss = price[0]
    for i in range(len(p_lst) - 1):
        if p_lst[i+1][0] < p_lst[i][0]:
            min_loss = min(min_loss, p_lst[i+1][1] - p_lst[i][1])
            
    return min_loss