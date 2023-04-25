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

    def distanceFrom(self, other):
        xDistance = self.x - other.getX()
        yDistance = self.y - other.getY()
        return (xDistance * 2 + yDistance ** 2) ** .5

    def __str__(self):
        return '<{}, {}>'.format(str(self.x), str(self.y))


class Drunk(object):
    def __init__(self, name: str = None):
        self.name = name

    def __str__(self):
        if self.name == None:
            return 'Anonymus'
        return self.name


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        return random.choice(stepChoices)


class Field(object):
    def __init__(self):
        self.drunks = {}

    def addDrunk(self, drunk: Drunk, location: Location):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = location

    def moveDrunk(self, drunk: Drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDistance, yDistance = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDistance, yDistance)
