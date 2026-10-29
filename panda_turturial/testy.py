import pandas as pd
pd.set_option("display.max_rows", 10)
pd.set_option("display.max_columns", 10)
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

#print(reviews.groupby(['country', 'variety']).variety.count().sort_values(ascending=False))

there = reviews.region_1.fillna('Unknown')

print(reviews.region_1.fillna('Unknown').value_counts(ascending=False))