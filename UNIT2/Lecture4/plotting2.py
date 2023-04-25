import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.5 ** i)

plt.figure('lin quad')
plt.clf()
plt.subplot(211)
plt.ylim(0, 900)
plt.plot(mySamples, myLinear, 'b', label='linear', linewidth=1.0)
plt.legend()
plt.title('Linear vs. Quadratic')
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(mySamples, myQuadratic, 'r', label='quadratic', linewidth=2.0)
plt.legend()

plt.figure('cub exp linear')
plt.clf()
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=1.0)
plt.legend()
plt.title('Cubic vs. Exponential lin')
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(mySamples, myExponential, 'r--', label='exponential', linewidth=2.0)
plt.legend()

plt.figure('cub exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=1.0)
plt.plot(mySamples, myExponential, 'r--', label='exponential', linewidth=2.0)
plt.yscale('log')
plt.title('Cubic vs. Exponential log')
plt.legend()

plt.show()