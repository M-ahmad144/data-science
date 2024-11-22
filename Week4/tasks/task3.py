import matplotlib.pyplot as plt
import numpy as np

# Define x ranges for the subplots
x_trig = np.linspace(-2 * np.pi, 2 * np.pi, 400)  # Range for trigonometric functions
x_exp = np.linspace(0, 5, 400)  # Range for exponential function

# Compute the functions
y_sin = np.sin(x_trig)  # y = sin(x)
y_cos = np.cos(x_trig)  # y = cos(x)
y_tan = np.tan(x_trig)  # y = tan(x)
y_exp = np.exp(x_exp)  # y = e^x

# Create the 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Top-left subplot: y = sin(x)
axs[0, 0].plot(x_trig, y_sin, color="b")
axs[0, 0].set_title("y = sin(x)")
axs[0, 0].grid(True)

# Top-right subplot: y = cos(x)
axs[0, 1].plot(x_trig, y_cos, color="r")
axs[0, 1].set_title("y = cos(x)")
axs[0, 1].grid(True)

# Bottom-left subplot: y = tan(x) with limits to avoid large spikes
axs[1, 0].plot(x_trig, y_tan, color="g")
axs[1, 0].set_ylim(-10, 10)  # Limiting y-axis to avoid extreme values
axs[1, 0].set_title("y = tan(x)")
axs[1, 0].grid(True)

# Bottom-right subplot: y = e^x
axs[1, 1].plot(x_exp, y_exp, color="m")
axs[1, 1].set_title("y = e^x")
axs[1, 1].grid(True)

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()
