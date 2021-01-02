
def bonAppetit(bill, k, b):
    cost = sum(bill)
    anna_cost = (cost - bill[k])//2
    if anna_cost == b:
        return "Bon Appetit"
    else:
        return b - anna_cost
    


print(bonAppetit([3,10,2,9], 1, 7))
print(bonAppetit([3,10,2,9], 1, 12))

