import pandas as pd
import random

from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from sklearn.model_selection import train_test_split

# Define possible values
genders = ['Female', 'Male']
reviews = ['Good', 'Average', 'Poor']
educations = ['School', 'UG', 'PG']  # UG = Undergraduate, PG = Postgraduate
purchased_options = ['Yes', 'No']

# Generate 50 rows
data = []
for _ in range(50):
    age = random.randint(10, 70)  # realistic age range
    gender = random.choice(genders)
    review = random.choice(reviews)
    education = random.choice(educations)
    purchased = random.choice(purchased_options)
    data.append([age, gender, review, education, purchased])

# Create DataFrame
df = pd.DataFrame(data, columns=['age', 'gender', 'review', 'education', 'purchased'])
# print(df)
# temp = pd.get_dummies(df, columns=['gender'], dtype=int, drop_first=True)
# print(temp)

counts = df['age'].value_counts()
df['age'].nunique()

threshold = 50
repl = counts[counts <= threshold].index
temp = pd.get_dummies(df['age'].replace(repl, 'below50'))
print(temp)

df = df.iloc[:, 2:]

xTrain, xTest, yTrain, yTest = train_test_split(df.iloc[:, 0:2], df.iloc[:, -1], test_size=0.2)
# print(xTrain)

oe = OrdinalEncoder(categories=[['Poor', 'Average', 'Good'], ['School', 'UG', 'PG']])
oe.fit(xTrain)
# print(oe.categories_)

xTrain = oe.transform(xTrain)
# print(xTrain)

le = LabelEncoder()
le.fit(yTrain)
# print(yTrain)

yTrain = le.transform(yTrain)
yTest = le.transform(yTest)
# print(yTrain)

