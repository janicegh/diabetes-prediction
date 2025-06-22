import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

# load data
df = pd.read_csv ('diabetes.csv')

# summary statistics
print(df.describe())

#check missing values
print(df.isnull().sum())

# Histogram of glucose
plt.figure(figsize=(8, 6))
sns.histplot(df['Glucose'], bins=30)
plt.title('Glucose Distribution')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
