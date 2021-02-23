from collections import deque
def topView(root):
    if not root:
        return
    
    result = {}
    key = 0
    root.key = key
    
    queue = deque()
    queue.append(root)
    while len(queue):
        root = queue[0]
        key = root.key 
         
        if key not in result:
            result[key] = root.info 
        
        if root.left:         
            root.left.key = key-1
            queue.append(root.left)  
        if root.right:         
            root.right.key = key+1
            queue.append(root.right) 
         
        queue.popleft()
    
    for i in sorted(result):
        print(result[i], end=" ")