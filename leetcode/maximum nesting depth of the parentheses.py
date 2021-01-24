def maxDepth(s):
    depth = 0
    par = 0
    for i in s:
        if i == '(':
            par += 1
            depth = max(depth, par)
        if i == ')':
            par -= 1
            depth = max(depth, par)
    return depth

print(maxDepth("(1+(2*3)+((8)/4))+1"))