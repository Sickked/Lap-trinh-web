import numpy as np
import matplotlib.pyplot as plt
universe = np.arange(0,11,1)
a = 3
b = 5
c = 7
membership = np.zeros_like(universe)
membership[(universe >=a)& (universe<=b)]=(universe[(universe>=a)&(universe<=b)]-a)/(b-a)
membership[(universe >=b)& (universe <=c)]=(c - universe[(universe >=b )&(universe <= c)])/(c-b)
plt.plot(universe, membership, 'b', linewidth=1.5)
plt.fill_between(universe, 0, membership, alpha=0.3)
plt.title('Hàm thuộc tam giác')
plt.xlabel('Giá trị')
plt.xlabel('Độ thuộc')
plt.grid(True)
plt.show()
