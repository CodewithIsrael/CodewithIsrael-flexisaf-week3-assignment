# Week 3 Assignment - Flexisaf Internship
# Create line plot, scatter plot, histograms, and box plots

# -------------------
# 1. Import Libraries
# -------------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# -------------------
# 2. Create / Load Dataset
# -------------------
# If you already have a CSV dataset, replace this part with:
# df = pd.read_csv("your_dataset.csv")

# For demonstration, let's create a simple dataset
np.random.seed(42)
df = pd.DataFrame({
    "Age": np.random.randint(18, 60, 100),
    "Salary": np.random.randint(20000, 100000, 100),
    "Balance": np.random.normal(50000, 15000, 100)
})

print("First 5 rows of dataset:")
print(df.head())

# -------------------
# 3. Line Plot (Matplotlib)
# -------------------
plt.figure()
plt.plot(df["Age"], df["Salary"], marker="o", linestyle="-", color="green")
plt.title("Line Plot of Salary vs Age")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# -------------------
# 4. Scatter Plot (Matplotlib)
# -------------------
plt.figure()
plt.scatter(df["Age"], df["Balance"], c="blue", alpha=0.6)
plt.title("Scatter Plot of Balance vs Age")
plt.xlabel("Age")
plt.ylabel("Balance")
plt.grid(True)
plt.show()

# -------------------
# 5. Histogram (Seaborn)
# -------------------
plt.figure()
sns.histplot(df["Salary"], kde=True, bins=20, color="purple")
plt.title("Histogram of Salary")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# -------------------
# 6. Box Plot (Seaborn)
# -------------------
plt.figure()
sns.boxplot(data=df[["Age", "Salary", "Balance"]], orient="h", palette="Set2")
plt.title("Box Plots of Age, Salary, and Balance")
plt.show()
