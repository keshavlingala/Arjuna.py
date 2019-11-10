# to avoid iterating through all the days in year
# instead taking a factor dictionary called paid where each day is mapped to a boolean value
def buymonth(cost, paid, day):
    cost += prices[2]
    # making days upto a month paid (paying for month)
    for i in range(days[day], days[day] + 30):
        if i in paid.keys():
            paid[i] = True
    return bt(days, prices, paid, cost, day + 1)


def buyday(cost, paid, day):
    # buying for a single day making it paid and moving forward
    cost += prices[0]
    paid[days[day]] = True
    return bt(days, prices, paid, cost, day + 1)


def buyweek(cost, paid, day):
    cost += prices[1]
    for i in range(days[day], days[day] + 7):
        # paying for a month changing in paid and moving to next day
        if i in paid.keys():
            paid[i] = True
    return bt(days, prices, paid, cost, day + 1)


def bt(days, prices, paid, cost, day):
    if all((p is True for p in paid.values())) or day >= len(days):
        # if all the days are already paid then return current cost
        # or number of days exceeded
        return cost
    if not paid[days[day]]:
        # taking a decision on every non paid day to buy either day | week | month pass and recursion to next day
        return min(buyday(cost, paid.copy(), day), buyweek(cost, paid.copy(), day), buymonth(cost, paid.copy(), day))
    if paid[days[day]]:  # if this day is already paid move to next day
        return bt(days, prices, paid, cost, day + 1)


days = [int(i) for i in input().split()]  # input days
prices = [int(i) for i in input().split()]  # input prices
paid = dict(zip(days, [False] * len(days)))  # creating a list with given number of days size
print(bt(days, prices, paid, cost=0, day=0))  # calling the recursion function initially for day 1
