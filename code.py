# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here

df = pd.read_csv(path)
df['state'] = df['state'].apply(str.lower)
df['total'] = df.loc[:,['Jan','Feb','Mar']].sum(axis=1)

sum_row = df[['Jan','Feb','Mar','total']].sum()

df_final = df.append(sum_row,ignore_index = True)

df_final.head(5)

# Code ends here


# --------------
import requests

# Code starts here

url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response = requests.get(url)



df1 = pd.read_html(response.content)[0]

df1 = df1.iloc[11:, :]

df1 = df1.rename(columns = df1.iloc[0, :]).iloc[1:, :]

df1['United States of America'] = df1['United States of America'].apply(lambda x: x.replace(' ', '')).astype(object)

# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here

df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = dict(zip(df1['United States of America'], df1['US']))

df_final['abbr'] = df_final.index[6]

df_final['abbr'] = df_final['state'].map(mapping)

# Code ends here


# --------------
# Code stars here

df_final.loc[df_final['state'] == 'mississipi', 'abbr'] = 'MS'
df_final.loc[df_final['state'] == 'tenessee', 'abbr'] = 'TN'

# Code ends here


# --------------
# Code starts here

df_sub = df_final.groupby(['abbr'])[['Jan', 'Feb', 'Mar', 'total']].sum()

formatted_df = df_sub.applymap(lambda x: "$" + str(x))

print(formatted_df)

# Code ends here


# --------------
# Code starts here

sum_row = pd.DataFrame(df_final[['Jan', 'Feb', 'Mar', 'total']].sum())

df_sub_sum = sum_row.transpose()

df_sub_sum = df_sub_sum.applymap(lambda x: "$" + str(x))

final_table = formatted_df.append(df_sub_sum)

print(final_table)

# Code ends here


# --------------
# Code starts here

df_sub['total'] = df_sub['Jan'] + df_sub['Feb'] + df_sub['Mar']
plt.pie(df_sub['total'])

# Code ends here


