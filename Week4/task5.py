#  - Objective: Understand how to visualize data distributions with histograms.
#  - Instructions:
#  1. Generate a dataset of 500 random numbers from a normal distribution (use
# `np.random.randn(500)`).
#  2. Plot a histogram of the data with 20 bins.
#  3. Customize the histogram by changing the color and edge color of the bars.
#  4. Add a title "Histogram of Random Data" and label the axes.
#  - Expected Output: A well-labeled histogram showing the distribution of the random data.

import matplotlib.pyplot as plt
import numpy as np

# Generate a dataset of 500 random numbers from a normal distribution
data = np.random.randn(500)

# Plot a histogram of the data with 20 bins
plt.hist(data, bins=20, color="skyblue", edgecolor="black")

# add a title
plt.title("Histogram of Random Data")

plt.show()
