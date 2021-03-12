import itertools
from collections import defaultdict

class Solution:
    def pyramidTransition(self, bottom: str, allowed: [str]) -> bool:
        children = defaultdict( list )
        
        for pair in allowed:
            children[ pair[:2]  ].append(pair[2])
            
            
        stack = [bottom]
        # result = False
        
        while stack:
            base = stack.pop()
            
            if len(base) == 1:
                return True
            
            nextBase = []
            for index in range(1, len(base)):
                color = base[index -1] + base[index]
                
                if color in children:
                    nextBase.append( children[color] )
                else:
                    break
                    
 
            if len( nextBase ) != len(base) - 1:
                continue

            stack += itertools.product(*nextBase)
        
        return False