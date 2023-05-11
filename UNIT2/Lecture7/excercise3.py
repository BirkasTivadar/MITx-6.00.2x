import sys


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import numpy as np
    if len(L) == 0:
        return float('NaN')
    else:
        return np.std([i for i in map(len, L)])


def teszt(sikeres_teszt):
    """  Egy teszt eredményének megjelenítése.  """
    sorszam = sys._getframe(1).f_lineno  # A hívó sorának száma
    if sikeres_teszt:
        msg = "A(z) {0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z) {0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)


L = ['a', 'z', 'p']
L2 = ['apples', 'oranges', 'kiwis', 'pineapples']
teszt(stdDevOfLengths(L) == 0)
teszt(abs(stdDevOfLengths(L2) - 1.8708) < 0.0001)
