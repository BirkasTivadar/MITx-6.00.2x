class Food(object):
    def __init__(self, name: str, value: float, calories: float):
        self.name = name
        self.value = value
        self.calories = calories

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.value / self.calories

    def __str__(self):
        return '{}: <{}, {}>'.format(self.name, str(self.value), str(self.calories))


def buildMenu(names: list, values: list, calories: list):
    """
    names, values, calories lists of same length
    """
    menu: list = []
    for i in range(len(names)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu


def greedy(items: list, maxCost: float, keyFunction: any):
    """
    Assumes maxCost >= 0
    :param keyFunction: maps elements of items to numbers
    """
    itemsCopy: list = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = .0, .0

    for i in range(len(itemsCopy)):
        actualCost = itemsCopy[i].getCost()
        if totalCost + actualCost <= maxCost:
            result.append(itemsCopy[i])
            totalCost += actualCost
            totalValue += itemsCopy[i].getValue()
    return (result, totalValue)


def testGreedy(items: list, constraint: float, keyFunction: any):
    taken, value = greedy(items, constraint, keyFunction)
    print('Total value of items taken = {}'.format(value))
    for item in taken:
        print('   {}'.format(item))


def testGreedys(foods: list, maxUnits: float):
    print('Use greedy by value to allocate {} calories'.format(maxUnits))
    testGreedy(foods, maxUnits, Food.getValue)

    print('\nUse greedy by cost to allocate {} calories'.format(maxUnits))
    testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))

    print('\nUse greedy by density to allocate {} calories'.format(maxUnits))
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut']
values = [89, 90, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
# testGreedys(foods, 750)
testGreedys(foods, 1000)
