import numpy as np
import pandas as pd
def load_data():
    # read the data from csv and save into dataframe
    df = pd.read_csv("olympics.csv", error_bad_lines=False)[0:]
    # Rename column containing 01, 02 and 03 to Gold, Silver and Bronze
    df.replace(['01 !', '02 !', '03 !'], ['Gold', 'Silver', 'Bronze'], inplace = True)
    # Split country name and country code and add country name as data frame index
    df['country_name'], df['country_code'] = df['0'].str.split('\xc2\xa0', 1).str
    # and add country name as data frame index
    df.set_index(['country_name'], append=True,inplace = True)
    # Drop the column Totals
    df.drop(df.index[-1], inplace= True)
    return df
    
# Question - 2:
# I m not sure about this, I did not understand what is the requirement,but I tried it
def first_country(df):
    for i in df.iloc[1]:
        print i,
        
# Question - 3:
def gold_medal(df):
    return df['2'][1:].astype(np.int64).idxmax()[1]

# Question - 4:
def biggest_difference_in_gold_medal(df):
    return (df['2'][1:].astype(np.int64) - df['7'][1:].astype(np.int64)).apply(lambda x: (x if x > 0 else -x)).idxmax()[1]
    
# Question - 5:
# seasion_wise_calculation of medals calculated
def seasion_wise_calculation(df, col1, col2, col3,):
    return df[col1][1:].astype(np.int64) * 3 + df[col2][1:].astype(np.int64) *2 + df[col3][1:].astype(np.int64) * 1

def get_points(df):
    df['Points'] = seasion_wise_calculation(df,'2','3','4') + seasion_wise_calculation(df,'7','8','9') +  \
        seasion_wise_calculation(df,'12','13','14')
    return df['Points']
    

# function calls    
df = load_data()
print(first_country(df))
print(gold_medal(df))
print(biggest_difference_in_gold_medal(df))
print(get_points(df))



f1 = df['2'][1].values
f2 = df['3'][1].values
f3 = df['4'][1].values

X=np.matrix(zip(f1,f2,f3))
kmeans = KMeans(n_clusters=3).fit(X)