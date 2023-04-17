import pylab as plt


def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate / 12
    for i in range(terms):
        base += [i]
        savings += [savings[-1] * (1 + mRate) + monthly]
    return base, savings


def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf()
    for monthly in monthlies:
        xValues, yValues = retire(monthly, rate, terms)
        plt.plot(xValues, yValues, label='retire: {}'.format(str(monthly)))
        plt.legend()


savingsMonthly = [500, 700, 900, 1100]
displayRetireWMonthlies(savingsMonthly, .05, 40 * 12)


def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xValues, yValues = retire(month, rate, terms)
        plt.plot(xValues, yValues, label='retire: {} : {}%'.format(str(month), str(int(rate * 100))))
        plt.legend()


ratesPerYear = [.03, .05, .07]
displayRetireWRates(800, ratesPerYear, 40 * 12)


def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure('retireBoth')
    plt.clf()
    plt.xlim(30 * 12, 40 * 12)
    monthLabels = ['r', 'b', 'g', 'k']
    rateLabels = ['-', '--', '-']
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i % len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j % len(rateLabels)]
            xValues, yValues = retire(monthly, rate, terms)
            plt.plot(xValues, yValues, monthLabel + rateLabel,
                     label='retire: {} : {}%'.format(str(monthly), str(int(rate * 100))), linewidth=(j % 3) + 1)
            plt.legend()


displayRetireWMonthsAndRates(savingsMonthly, ratesPerYear, 40 * 12)
plt.show()