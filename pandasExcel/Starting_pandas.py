import pandas as pd
import numpy as np

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
             'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

index = range(101, 108)

df = pd.DataFrame(data, index=index)

type(df)

df.index

df.columns

type(df.columns)

df.head(3)
df.tail()

# columns

df["city"]

type(df["city"])

cities = df["city"]

cities

cities.index

df.age

df.py-score

df["py-score"]

# row

df.index

df.loc[103]

type(df.loc[103])

cities[103]

# different ways of creating DF

d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}
pd.DataFrame(d)

pd.DataFrame(d, index=[100, 200, 300], columns=['z', 'y', 'x'])

l = [{'x': 1, 'y': 2, 'z': 100},
     {'x': 2, 'y': 4, 'z': 100},
     {'x': 3, 'y': 8, 'z': 100}]

pd.DataFrame(l)

l = [[1, 2, 100],
     [2, 4, 100],
     [3, 8, 100]]

pd.DataFrame(l, columns=['x', 'y', 'z'])

arr = np.array([[1, 2, 100],
                [2, 4, 100],
                [3, 8, 100]])

df_ = pd.DataFrame(arr, columns=['x', 'y', 'z'], copy=True)  # copy if you want to create a new reference

arr[1, 1] = 33

# from files
df.to_csv('/mnt/WORKSPACE/dcr_workspace/gitral/PythonLearning/pandasExcel/data.csv')

pd.read_csv('data.csv', index_col=0)

df.to_csv("job_candidate.csv")

jd = pd.read_csv("job_candidate.csv", index_col=0)

import os
print(os.path.dirname(os.path.realpath(__file__)))

# getting data

df.index

df.index[1]

df.columns

df.columns[2]

df.index = np.arange(10, 17)

df.values

df.to_numpy()

df.dtypes

df_ = df.astype(dtype={'age': np.int32, 'py-score': np.float32})

df_.dtypes

df.ndim

df.size

df.shape

df.memory_usage()

df_.memory_usage()



# col

df["name"]

df.age

# rows by labels

df.loc[11]

#piece of df

df.loc[:, ["age", "py-score"]]

# even rows

df.loc[[x for x in df.index if not x % 2]]

# even rows and some columns

df.loc[[x for x in df.index if not x % 2], ["name", "city"]]

# getting data using integer indexes

df.iloc[0, [0,2]]

df.iloc[:, [0,2]]

df.iloc[[0,2], :]

# same
df.loc[12, "city"]
# with at you can only get individual elements
df.at[12, "city"]
df.iat[2,1]

# modifying values

df.loc[:13, "py-score"] = [40, 50, 60, 70]

df.loc[14:, "py-score"] = 0

df.iloc[:, -1] = np.linspace(20, 50, len(df)) # method to put a range equally spaced over a length

df.loc[16] = ["Jack", "Chicago", 29, 70]

df.loc[11, "city"] = "Ottawa"

# add and remove records

john = pd.Series(data=['John', 'Boston', 34, 79],
                 index=df.columns, name=17)

df = df.append(john)

df = df.drop(labels=[17])

df.drop(labels=[16], inplace=True)

# add and remove columns

df['js-score'] = np.array([71.0, 95.0, 88.0, 79.0, 91.0, 91.0, 80.0])

df['total-score'] = 0.0

df.insert(loc=4, column='django-score',
          value=np.array([86.0, 81.0, 78.0, 88.0, 74.0, 70.0, 81.0]))

# removing

del df['total-score']

total_score = df.pop("total-score")
df = df.drop(labels='age', axis=1)

# operations

df["js-score"] * 2

df["js-score"] / 4

df['py-score'] + df['js-score']

df['total'] =\
    0.4 * df['py-score'] + 0.3 * df['django-score'] + 0.3 * df['js-score']

del df['total']

df['total'] = np.average(df.iloc[:, 3:6], axis=1,
                         weights=[0.4, 0.3, 0.3])

# sorting

df.sort_values(by='js-score', ascending=False)

df.sort_values(by=['js-score', "py-score"], ascending=[False, False]) # pass inplace to modify the df

# filtering
filter_ = df['django-score'] >= 80
filter_
df[filter_]

df[(df['py-score'] >= 80) & (df['js-score'] >= 80)] # use & because you want elementwise boolean

df[(df['py-score'] >= 80) | (df['js-score'] >= 80)] # use | because you want elementwise boolean

df['django-score'].where(cond=df['django-score'] >= 80, other=0.0)

df.filter(items=["py-score", "django-score", "js-score"]) # filter by columns

df.filter(like="score")

df.filter(like="score", axis=0) # you can use axis to do the same on rows

df.filter(regex="*e") # ?? doesnt work

# Determining Data Statistics

df.describe()

df["py-score"].mean()
df["py-score"].std()

df.mean()

# handling missing data

df_ = pd.DataFrame({'x': [1, 2, np.nan, 4]})

df_.mean()

df_.mean(skipna=False)

df_.fillna(value=0)

df_.fillna(method='ffill')

df_.fillna(method='bfill')

df_.interpolate()

df_.dropna()

# Iterating Over a Pandas DataFrame

# Cols
for col_label, col in df.items():
    print(col_label, col, sep='\n', end='\n\n')

# rows
for row_label, row in df.iterrows():
    print(row_label, row, sep='\n', end='\n\n')

for row in df.loc[:, ['name', 'city', 'total']].itertuples():
    print(row)

for row in df.loc[:, ['name', 'city', 'total']].itertuples(index=False, name="Candidate"):
    print(row)

# time series
temp_c = [ 8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0,
           9.1, 12.8, 15.3, 19.1, 21.2, 22.1, 22.4, 23.1,
          21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]

dt = pd.date_range(start='2019-10-27 00:00:00.0', periods=24,
                   freq='H')

type(dt)

temp = pd.DataFrame(data={'temp_c': temp_c}, index=dt)

temp['2019-10-27 05':'2019-10-27 15']

# grouping data
temp.resample(rule='6h').mean()
temp.resample(rule='6h').min()

# rolling-window analysis
#take oprevius values to get next in this case 3 previus data
temp.rolling(window=3).mean()

#plotting

import matplotlib.pyplot as plt
temp.plot()
plt.show()

temp.plot().get_figure().savefig('temperatures.png')

