# news_perf.py
import timeit
import numpy as np

from news import df

def run_apply():
    # Version 1: using `.apply()`
    df.groupby("outlet", sort=False, observed=True)["title"].apply(
        lambda ser: ser.str.contains("Fed").sum()
    ).nlargest(10)

def run_vectorization():
    #Version 2: using vectorization
    mentions_fed = df["title"].str.contains("Fed")
    mentions_fed.groupby(
        df["outlet"], sort=False, observed=True
    ).sum().nlargest(10).astype(np.uintc)

print(f"Version 1: {timeit.timeit(run_apply, number=3)}")
print(f"Version 2: {timeit.timeit(run_vectorization, number=3)}")
