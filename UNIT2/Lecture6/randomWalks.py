from rwClasses import *


def walk(field: Field, drunk: Drunk, numberSteps: int):
    """
    Assumes: drunk in field, and numSteps an int >= 0.
    Moves drunk numberSteps times, and returns the distance between
    the final location and the location at the start of the walk.
    """
    start = field.getLocation(drunk)
    for step in range(numberSteps):
        field.moveDrunk(drunk)
    return start.distFrom(field.getLocation(drunk))


def simulationWalks(numberSteps: int, numberTrials: int, drunkClass):
    """
    Assumes numberSteps an int >= 0, numberTrials an int > 0,
    dClass a subclass of Drunk
    Simulates numberTrials walks of numberSteps steps each.
    Returns a list of the final distances for each trial.
    """
    Homer = drunkClass()
    origin = Location(0, 0)
    distances: list = []
    for trial in range(numberTrials):
        field = Field()
        field.addDrunk(Homer, origin)
        distances.append(round(walk(field, Homer, numberSteps), 1))
    return distances


def drunkTest(walkLengths, numberTrials: int, dClass):
    """
    Assumes walkLengths >= 0, numberTrials > 0
    For each number of steps in walkLengths,
        runs simulationWalks with numberTrials walks and prints results
    """
    for numberSteps in walkLengths:
        distances = simulationWalks(numberSteps, numberTrials, dClass)
        print(dClass.__name__, 'random walk of', numberSteps, 'steps')
        print(' Mean =', round(sum(distances) / len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))


# random.seed(0)
# drunkTest((10, 1000, 1000, 10000), 100, UsualDrunk)


class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1),
                       (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)


def simulationAll(drunkKinds, walkLengths, numberTrials):
    for drunkClass in drunkKinds:
        drunkTest(walkLengths, numberTrials, drunkClass)


random.seed(0)
simulationAll((UsualDrunk, ColdDrunk), (1, 10, 100, 1000, 10000), 100)
