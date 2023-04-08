from UNIT1.Lecture1.greedy import *


def maxValue(toConsider: list, available: float):
    """
    Assumes toConsider a list of items, avail a weight
    Returns a tuple of the total value of a solution to the 0/1 knapsack problem and the items of that solution
    """
    if toConsider == [] or available == 0:
        result = (0, ())
    elif toConsider[0].getCost() > available:
        # Explore right branch only
        result = maxValue(toConsider[1:], available)
    else:
        nextItem = toConsider[0]

        # Explore left branch
        withValue, withToTake = maxValue(toConsider[1:], available - nextItem.getCost())
        withValue += nextItem.getValue()
        # Explore right branch

        withoutValue, withoutToTake = maxValue(toConsider[1:], available)

        # Choose better branch
        if withValue > withoutValue:
            result = (withValue, withToTake + (nextItem,))
        else:
            result = (withoutValue, withoutToTake)
    return result


def testMaxValue(foods: list, maxUnits: float):
    print('Use search tree to allocate {} calories'.format(maxUnits))
    value, taken = maxValue(foods, maxUnits)
    print('Total value of items taken = {}'.format(value))
    for item in taken:
        print('   {}'.format(item))


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)

testGreedys(foods, 750)
print('')
testMaxValue(foods, 750)
