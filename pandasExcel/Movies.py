# https://www.dataquest.io/blog/excel-and-pandas/

import pandas as pd
import matplotlib.pyplot as plt

# Read data from the Excel file
from xlsxwriter import worksheet
from xlsxwriter import workbook


excel_file = '/mnt/WORKSPACE/dcr_workspace/TMP/excel_mani/movies.xls'
movies = pd.read_excel(excel_file)
# movies.head()

movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
movies_sheet1.head()

movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
movies_sheet2.head()

movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
movies_sheet3.head()

movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

movies.shape
# same but with constructor
xlsx = pd.ExcelFile(excel_file)
movies_sheets = []
for sheet in xlsx.sheet_names:
    movies_sheets.append(xlsx.parse(sheet))
movies = pd.concat(movies_sheets)

# Exploring

movies.shape

movies.head()

movies.tail()

sorted_by_gross = movies.sort_values(['Gross Earnings'], ascending=False)
sorted_by_gross["Gross Earnings"].head(10)

sorted_by_gross['Gross Earnings'].head(10).plot(kind="barh")
plt.show()

movies['IMDB Score'].plot(kind="hist")
plt.show()

# Getting statistical information about the data

movies.describe()

movies["Year"].mean()

# Reading files with no header and skipping records

movies_skip_rows = pd.read_excel("/mnt/WORKSPACE/dcr_workspace/TMP/excel_mani/moviesMess.xls", header=None, skiprows=4)
movies_skip_rows.head(5)

movies_skip_rows.columns = ['Title', 'Year', 'Genres', 'Language', 'Country', 'Content Rating', 'Duration', 'Aspect Ratio', 'Budget',
                            'Gross Earnings', 'Director', 'Actor 1', 'Actor 2', 'Actor 3', 'Facebook Likes - Director', 'Facebook Likes - Actor 1',
                            'Facebook Likes - Actor 2', 'Facebook Likes - Actor 3', 'Facebook Likes - cast Total', 'Facebook likes - Movie',
                            'Facenumber in posters', 'User Votes', 'Reviews by Users', 'Reviews by Crtiics', 'IMDB Score']
movies_skip_rows.head()

# Reading a subset of columns

movies_subset_columns = pd.read_excel(excel_file, usecols=list(range(0, 7)))
movies_subset_columns.head()

# Applying formulas on the columns
movies["Net Earnings"] = movies["Gross Earnings"] - movies["Budget"]

sorted_movies = movies[['Net Earnings']].sort_values(['Net Earnings'], ascending=[False])
sorted_movies.head(10)['Net Earnings'].plot.barh()
plt.show()

# Pivot Table in pandas

movies_subset = movies[['Year', 'Gross Earnings']]
movies_subset.head()

earnings_by_year = movies_subset.pivot_table(index=['Year'])
earnings_by_year.head()

earnings_by_year.plot()
plt.show()

movies_subset = movies[['Country', 'Language', 'Gross Earnings']]
movies_subset.head()

earnings_by_co_lang = movies_subset.pivot_table(index=['Country', 'Language'])
earnings_by_co_lang.head()

earnings_by_co_lang.head(20).plot(kind='bar', figsize=(20,8))
plt.show()

# Exporting the results to Excel

movies.to_excel('output.xlsx')

movies.head()

movies.to_excel('output.xlsx', index=False)

# Nicer

writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
movies.to_excel(writer, index=False, sheet_name='report')
workbook = writer.bookworksheet = writer.sheets['report']

# this doesn't work
header_fmt = workbook.add_format({'bold': True})
worksheet.set_row(0, None, header_fmt)

writer.save()


######
raw_data = {'first_name': ['Sheldon', 'Raj', 'Leonard', 'Howard', 'Amy'],
            'last_name': ['Copper', 'Koothrappali', 'Hofstadter', 'Wolowitz', 'Fowler'],
            'age': [42, 38, 36, 41, 35],
            'Comedy_Score': [9, 7, 8, 8, 5],
            'Rating_Score': [25, 25, 49, 62, 70]}

df = pd.DataFrame(raw_data, columns=['first_name', 'last_name', 'age',
                                     'Comedy_Score', 'Rating_Score'])

print(df)

print(df['Comedy_Score'].where(df['Rating_Score'] < 50))

name = df.loc[df['age'] == 42]["first_name"].astype(str)

genotyping_name = project_df.loc[project_df['Sample-name'] == "104197-124"]["Genotyping-name"].to_string(index=False)







