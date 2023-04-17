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
plt.title('Linear vs. Quadratic')
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0)
plt.legend()
# plt.legend(loc='upper left')

plt.figure('cub exp')
plt.clf()
plt.title('Cubic vs. Exponential')
plt.xlabel('sample points')
plt.ylabel('cubic function')
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=4.0)
plt.plot(mySamples, myExponential, 'r--', label='exponential', linewidth=5.0)
plt.legend()

plt.show()
