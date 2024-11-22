import matplotlib.pyplot as plt
import numpy as np

# Create data for the plot
x = np.linspace(-10, 10, 400)  # 400 points between -10 and 10
y = 2 * x + 3

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="y = 2x + 3", color="b")

# Adding labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Line Plot")

# Show the plot
plt.grid(True)
plt.show()
