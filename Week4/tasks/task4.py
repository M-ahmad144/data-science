import matplotlib.pyplot as plt

# Data
departments = ["CS", "IT", "EE", "ME"]
enrollments = [150, 120, 100, 80]

# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(departments, enrollments, color="skyblue")
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.title("Department-wise Enrollment")
plt.show()

# Pie Chart
plt.figure(figsize=(10, 6))
plt.pie(enrollments, labels=departments, autopct="%1.1f%%")
plt.title("Department-wise Enrollment")
plt.show()
