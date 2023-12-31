

import pandas as pd
titanic_data = pd.read_csv("/content/train.csv")

titanic_data.shape

print("First few rows of the dataset:")
print(titanic_data.head())

print("Number of unique values in the 'Pclass' column:")
print(titanic_data['Pclass'].nunique())

print("\nSummary statistics of numerical columns:")
print(titanic_data.describe())

print("\nNumber of missing values in each column:")
print(titanic_data.isnull().sum())


print("Shape of the dataset before removing 'Cabin' column:", titanic_data.shape)

titanic_data.drop(columns=['Cabin'], inplace=True)

print("Shape of the dataset after removing 'Cabin' column:", titanic_data.shape)

median_age = titanic_data['Age'].median()
titanic_data['Age'].fillna(median_age, inplace=True)


titanic_data.dropna(inplace=True)

print("\nNumber of null values in each column after removal:")
print(titanic_data.isnull().sum())

titanic_data.shape

titanic_data = pd.get_dummies(titanic_data, columns=['Sex', 'Embarked'], drop_first=True)

print(titanic_data.head())

print("\nAverage fare paid by passengers in each class:")
print(titanic_data.groupby('Pclass')['Fare'].mean())


titanic_data['FamilySize'] = titanic_data['SibSp'] + titanic_data['Parch'] + 1

age_bins = [0, 18, 35, 50, 100]
age_labels = ['Child', 'Young Adult', 'Adult', 'Senior']
titanic_data['AgeGroup'] = pd.cut(titanic_data['Age'], bins=age_bins, labels=age_labels)

print("\nProcessed dataset after adding new features:")
print(titanic_data[['FamilySize', 'AgeGroup']].head())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.countplot(x='Pclass', data=titanic_data, palette='Set1')
plt.title('Passenger Count in Each Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(titanic_data['Age'], bins=20, kde=True, color='skyblue')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

correlation_matrix = titanic_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()
