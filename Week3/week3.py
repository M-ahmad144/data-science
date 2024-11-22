import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define the number of students
num_students = 100

# Generate random data for each attribute
data = {
    "GPA": np.round(np.random.uniform(2.0, 4.0, num_students), 2),
    "Age": np.random.randint(18, 30, num_students),
    "Study Hours/Week": np.random.randint(5, 40, num_students),
    "Location": np.random.choice(['Urban', 'Rural', 'Suburban'], num_students),
    "Sleep Hours": np.random.randint(4, 10, num_students),
    "Gender": np.random.choice(['Male', 'Female', 'Other'], num_students)
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# 1. Visualize GPA distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['GPA'], kde=True, bins=10, color='skyblue')
plt.title('Distribution of GPA')
plt.xlabel('GPA')
plt.ylabel('Frequency')
plt.show()

# 2. Scatter plot of Age vs. Study Hours/Week
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Study Hours/Week', hue='Gender', data=df, palette='Set1')
plt.title('Age vs. Study Hours/Week')
plt.xlabel('Age')
plt.ylabel('Study Hours/Week')
plt.legend(title='Gender')
plt.show()

# 3. Gender distribution (bar chart)
plt.figure(figsize=(8, 5))
sns.countplot(x='Gender', data=df, palette='pastel')
plt.title('Gender Distribution')
plt.ylabel('Number of Students')
plt.show()

# 4. Box plot of Study Hours/Week by Location
plt.figure(figsize=(10, 6))
sns.boxplot(x='Location', y='Study Hours/Week', data=df, palette='Set3')
plt.title('Study Hours per Week by Location')
plt.xlabel('Location')
plt.ylabel('Study Hours/Week')
plt.show()
