import random

random.seed(0)


def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])


def testRoll(n=10):
    for i in range(n):
        print(rollDie())


def runSim(goal, numberOfTrials):
    total = 0
    lenGoal = len(goal)
    for i in range(numberOfTrials):
        result = ''
        for i in range(lenGoal):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability = {}'.format(round(1 / (6 ** lenGoal), 8)))
    estimatedProbability = round(total / numberOfTrials, 8)
    print('Estimated probability = {}'.format(estimatedProbability))


# runSim('111111', 10000000)

def fracBoxCars(numberOfTests):
    numberOfBoxCars = 0
    for i in range(numberOfTests):
        if rollDie() == 6 and rollDie() == 6:
            numberOfBoxCars += 1
    return (numberOfBoxCars / numberOfTests) * 100


print('Frequency of double 6 = {}%'.format(fracBoxCars(100000)))
