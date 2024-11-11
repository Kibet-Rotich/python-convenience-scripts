import pandas as pd
df = pd.read_csv('rotich.csv')

df['Phone number'] = df['Phone number'].astype(int)


df.to_csv('int_rotich.csv', index=False)