class Solution:
    def findRestaurant(self, list1: [str], list2: [str]) -> [str]:
        restaurants1, restaurants2 = set(list1), set(list2)
        commons = list(restaurants1.intersection(restaurants2))
        
        if len(commons) == 1:
            return commons
        
        hashmap = {}
        for fav in commons:
            hashmap[fav] = list1.index(fav) + list2.index(fav)
        
        hashmap = {key: value for key, value in sorted(hashmap.items(), key = lambda item: item[1])}
        
        result = []
        for item in hashmap:
            if len(result) == 0: result.append(item)
            elif hashmap[result[-1]] == hashmap[item]:
                result.append(item)
        
        return result
        