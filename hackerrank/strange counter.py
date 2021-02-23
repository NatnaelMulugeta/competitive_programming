def strangeCounter(t):
    start = 3
    
    while start*2 - 2 <= t:
        next_start = start * 2
        start = next_start
    
    value = start - (t - (start - 2))
    return value