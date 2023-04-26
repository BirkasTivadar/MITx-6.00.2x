import random


class Location(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, deltaX: float, deltaY: float):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        xDist = self.x - other.getX()
        yDist = self.y - other.getY()
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __str__(self):
        return '<{}, {}>'.format(self.x, self.y)


class Drunk(object):
    def __init__(self, name: str = None):
        self.name = name

    def __str__(self):
        if self.name == None:
            return 'Anonymous'
        return self.name


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk: Drunk, location: Location):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = location

    def isDrunkInField(self, drunk: Drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')

    def moveDrunk(self, drunk: Drunk):
        self.isDrunkInField(drunk)
        xDistance, yDistance = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDistance, yDistance)

    def getLocation(self, drunk: Drunk):
        self.isDrunkInField(drunk)
        return self.drunks[drunk]


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)


class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 0.9), (0.0, -1.1),
                       (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)
