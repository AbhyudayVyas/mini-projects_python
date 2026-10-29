import pandas as pd
pd.set_option("display.max_rows", 10)
reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

# monkey brain way
reviews["ratio"] = reviews.points / reviews.price

highest = 0
for i in reviews['points']:
    if i>highest: highest = i

print(reviews.title.loc[highest])


# alternative/preferred/pandas_kinda_ way to find the best bargain
reviews["ratio"] = reviews.points / reviews.price
highest = reviews.ratio.idxmax()
bargain_wine = reviews.title.loc[highest]

# _NOW_ shortening it to a single line of code
bargain_wine = reviews.title.loc[(reviews.points/reviews.price).idxmax()]