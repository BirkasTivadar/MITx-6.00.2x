from brutalForce import *
import random


def buildLargeMenu(numberOfItems, maxValue, maxCost):
    items = []
    for i in range(numberOfItems):
        items.append(Food(str(i),
                          random.randint(1, maxValue),
                          random.randint(1, maxCost)))
    return items


def fastMaxValue(toConsider, available, memo=None):
    """
    Assumes toConsider a list of subjects, avail a weight
    memo supplied by recursive calls
    Returns a tuple of the total value of a solution to the
    0/1 knapsack problem and the subjects of that solution
    """
    if memo is None:
        memo = {}
    if (len(toConsider), available) in memo:
        result = memo[(len(toConsider), available)]
    elif toConsider == [] or available == 0:
        result = (0, ())
    elif toConsider[0].getCost() > available:
        # Explore right branch only
        result = fastMaxValue(toConsider[1:], available, memo)
    else:
        nextItem = toConsider[0]
        # Explore left branch
        withValue, withToTake = fastMaxValue(toConsider[1:], available - nextItem.getCost(), memo)
        withValue += nextItem.getValue()
        # Explore right branch
        withoutValue, withoutToTake = fastMaxValue(toConsider[1:], available, memo)
        # Choose better branch
        if withValue > withoutValue:
            result = (withValue, withToTake + (nextItem,))
        else:
            result = (withoutValue, withoutToTake)
    memo[(len(toConsider), available)] = result
    return result


def testMaxValue(foods: list, maxUnits: float, algorithm, printItems=True):
    print('Menu contains {} items'.format(len(foods)))
    print('Use search tree to allocate {} calories'.format(maxUnits))
    value, taken = algorithm(foods, maxUnits)
    if printItems:
        print('Total value of items taken = {}'.format(value))
        for item in taken:
            print('   {}'.format(item))


for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45, 502):
    items = buildLargeMenu(numItems, 90, 250)
    testMaxValue(items, 750, fastMaxValue, False)
