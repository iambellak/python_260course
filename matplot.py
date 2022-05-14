import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-20,9,10)
y=x**2
plt.plot(x,y,'b')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Representation of Square Function')
plt.show() 