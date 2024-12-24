import matplotlib.pyplot as plt
import numpy as np


# Variables for initial population
glasgow_p = 635000
dharvi_p = 1000000

# Variable for growth rate
glasgow_r = 0.005
dharvi_r = 0.05 # growth rate = birth rate - death arte


t = np.linspace(0, 20, 100)

# Formula for population growth
population_glasgow = glasgow_p * np.exp(glasgow_r * t)
population_dharavi = dharvi_p * np.exp(dharvi_r * t)

# Plotting lines
plt.plot(t, population_glasgow, label="Glasgow Population", color='blue')
plt.plot(t, population_dharavi, label="Dharavi Population", color='red')

# Show population on specific points on line
for i in range(0, len(t), 5):
    plt.text(t[i], population_glasgow[i], f"{int(population_glasgow[i]):,}", fontsize=8, ha='right', color='blue')
    plt.text(t[i], population_dharavi[i], f"{int(population_dharavi[i]):,}", fontsize=8, ha='left', color='red', )

# Create tile and names and display
plt.xlabel('Years')
plt.ylabel('Population')
plt.title('Population Growth of Glasgow and Dharavi')
plt.legend()
plt.grid(True)
plt.show()