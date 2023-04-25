import random


def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 12


def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    return random.randrange(10, 22, 2)



