import matplotlib.pyplot as plt
import numpy as np

# Create data for the functions
x = np.linspace(-10, 10, 400)  # array of evenly spaced values between -10 and 10
y1 = x**2  # y = x^2
y2 = x**3  # y = x^3

# Create the plot
plt.figure(figsize=(8, 6))  # Create a figure with a specified size

# Plot y = x^2 with customizations
plt.plot(x, y1, color="r", linestyle="-", marker="o", label="y = x^2")

# Plot y = x^3 with customizations
plt.plot(x, y2, color="g", linestyle="--", marker="x", label="y = x^3")

# Adding gridlines with a dashed style
plt.grid(True, linestyle="--")


# Show the plot
plt.show()
