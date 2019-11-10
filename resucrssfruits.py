def stai(off, reqd, stack):  # check if an offer can be bought or not
    for i in range(len(reqd)):
        if (reqd[i] - stack[i]) < off[i]:  # if any fruits exceeded limit then false
            return False
    return True


def bestPlan(offers, fruits, reqd, cost, stack):
    finalcost = []
    for off in offers:  # for all offers available
        if stai(off[:-1], reqd, stack):
            # if offer satisfies
            # =============================================================================
            buystack = stack.copy()
            for i in range(len(stack)):                                                     # buy it
                buystack[i] += off[i]
            # =============================================================================
            # and add to cost and continue with the process
            finalcost.append(bestPlan(offers, fruits, reqd, cost + off[-1], buystack))
    # if not offers are satisfied then buy remaing fruits to fill requirement and return total cost
    if not any(finalcost):
        for i in range(len(fruits)):
            cost += (reqd[i] - stack[i]) * fruits[i]
        return cost
    # find the min of all plans and return
    return min(finalcost)


# =============================================================================
fruits = [int(a) for a in input().split()]
try:
    noff = int(input())
except ValueError:
    noff=int(input().split()[0])
offers = [[int(a) for a in input().split()] for i in range(noff)]               # input
reqd = [int(a) for a in input().split()]
# =============================================================================

# find the direct individual cost
indicost = 0
for i in range(len(fruits)):
    indicost += reqd[i] * fruits[i]
# print min of individual cost or best of all plans
print(min(indicost, bestPlan(offers, fruits, reqd, 0, [0] * len(reqd))))
