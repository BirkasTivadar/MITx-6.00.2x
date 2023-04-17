import random


def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])


def testRoll(n=10):
    for i in range(n):
        print(rollDie())

testRoll(5)