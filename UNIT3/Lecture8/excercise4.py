def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    # Your code here
    import random

    if numTrials == 0:
        return 'numTrials must be greater than zero'

    counter = 0.0
    for i in range(numTrials):
        bucket = ['RED', 'RED', 'RED', 'GREEN', 'GREEN', 'GREEN']

        choice1 = random.choice(bucket)
        bucket.remove(choice1)
        choice2 = random.choice(bucket)
        bucket.remove(choice2)
        choice3 = random.choice(bucket)
        bucket.remove(choice3)

        if choice1 == choice2 == choice3:
            counter += 1

    return counter / numTrials


print(noReplacementSimulation(1000))
