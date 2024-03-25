#Author: Gustavo Fernandes
import numpy as np  # import numpy library
import matplotlib.pyplot as plt  # import matplotlib library

normalrandom = np.random.normal(loc=5, scale=2, size=100) 
plt.hist(normalrandom, bins=30)  
plt.show() 

x = np.random.randint(0, 10, 100)  
h = x**3  
plt.plot(x, h)  
plt.xlabel('x') 
plt.ylabel('h(x)')  
plt.title('Plot of h(x) = x^3')  
plt.show() 

