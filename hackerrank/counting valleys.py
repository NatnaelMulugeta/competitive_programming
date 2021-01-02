def countingValleys(steps, path):
    valley_count = 0
    height = 0
    for i in range(steps):
        if path[i] == 'D':
            height -= 1
        elif path[i] == 'U':
            height += 1
            if height == 0:
                valley_count += 1
    return valley_count
