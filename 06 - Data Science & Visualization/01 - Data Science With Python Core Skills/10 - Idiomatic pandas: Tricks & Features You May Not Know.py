import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd
    import numpy as np

    return np, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## now testing lib doesn't exist anymore, we can use numpy random lib to generate random data..
    """)
    return


@app.cell
def _(np, pd):
    rng = np.random.default_rng(seed=42)

    sample_size = 10

    df = pd.DataFrame({
        'user_id': rng.integers(1000, 99999, size=sample_size),
        'score': rng.normal(loc=70, scale=10, size=sample_size),
        'group': rng.choice(['A', 'B', 'C'], size=sample_size)
    })
    df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Accessor Methods
    """)
    return


@app.cell
def _(pd):
    pd.Series._accessors
    return


@app.cell
def _(pd):
    addr = pd.Series(
        [
            'Washington, D.C. 20003',
            'Brooklyn , NY 11211-1755',
            'Omaha, NE 68154',
            'Pittsburgh, PA 15211',
        ]
    )

    addr
    return (addr,)


@app.cell
def _():
    s = 'hello'
    return (s,)


@app.cell
def _(s):
    s.upper()
    return


@app.cell
def _(addr, upper):
    addr.apply(upper)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## this is the accessor:
    """)
    return


@app.cell
def _(addr):
    addr.str.upper()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## let's try with a dataframe:
    """)
    return


@app.cell
def _(pd):
    kids = pd.DataFrame({
        'name': ['John', 'Dylan'],
        'age': [8, 10]
    })

    kids
    return (kids,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## we need to convert all columns to string; map a function to all elements, use the accessor 'str' to call .upper():
    """)
    return


@app.cell
def _(kids):
    kids.astype('str').map(str.upper)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    using a count to count number of digits in addr's zip code string:
    """)
    return


@app.cell
def _(addr):
    addr.str.count(r'\d')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Now with Daterange:
    """)
    return


@app.cell
def _(pd):
    dr_index = pd.date_range(start='2019', end='2021', freq='QE')

    daterng = pd.Series(pd.date_range('2019', periods=9, freq='QE'))

    type(dr_index)
    return (daterng,)


@app.cell
def _(daterng):
    daterng.dt.day_name()
    return


@app.cell
def _(daterng):
    daterng[daterng.dt.quarter > 2]
    return


@app.cell
def _(daterng):
    daterng[daterng.dt.is_year_end]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## DateTime Index
    """)
    return


@app.cell
def _():
    from itertools import product

    return (product,)


@app.cell
def _(np, pd, product):
    datecols = ['year', 'month', 'day']

    datecolumns = pd.DataFrame(list(product([2019, 2020], [1,2], [1, 2, 3])), columns=datecols)

    datecolumns['data'] = np.random.randn(len(datecolumns))
    return datecols, datecolumns


@app.cell
def _(datecolumns):
    datecolumns
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## to convert index to the datetimes:
    """)
    return


@app.cell
def _(datecols, datecolumns, pd):
    datecolumns.index = pd.to_datetime(datecolumns[datecols])
    return


@app.cell
def _(datecolumns):
    datecolumns
    return


@app.cell
def _(datecols, datecolumns):
    datecolumns.drop(datecols, inplace=True, axis=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Convert to series we use squeeze:
    """)
    return


@app.cell
def _(datecolumns):
    datecolumns.squeeze()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Categorical Data to save time
    """)
    return


@app.cell
def _(pd):
    colors = pd.Series([
      'periwinkle',
      'mint green',
      'burnt orange',
      'periwinkle',
      'burnt orange',
      'rose',
      'rose',
      'mint green',
      'rose',
      'navy',
    ])
    return (colors,)


@app.cell
def _(colors):
    colors
    return


@app.cell
def _(colors):
    mapper = {v: k for k, v in enumerate(colors.unique())}
    return (mapper,)


@app.cell
def _(mapper):
    mapper
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## this creates a code for each value, so we can have a dataframe using the codes and not the values, so saving a lot of space
    """)
    return


@app.cell
def _(colors, mapper):
    colors.map(mapper)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## we can achieve this with the category accessor method:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    we need to convert the data type to cateory:
    """)
    return


@app.cell
def _(colors):
    ccolors = colors.astype('category')
    return (ccolors,)


@app.cell
def _(ccolors):
    ccolors.cat.categories
    return


@app.cell
def _(ccolors):
    ccolors.cat.codes
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    but the dataframe becomes more difficult to maniplute the data. example, adding a new color:
    """)
    return


@app.cell
def _(ccolors):
    ccolors.iloc[5] = 'new color'
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    we need to add a new category first, then add the new color:
    """)
    return


@app.cell
def _(ccolors):
    ccolors_new=ccolors.cat.add_categories(['new color'])
    return (ccolors_new,)


@app.cell
def _(ccolors_new):
    ccolors_new.iloc[5] = 'new color'
    return


@app.cell
def _(ccolors_new):
    ccolors_new.cat.categories
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## introspect Groupby Objects via iteration
    """)
    return


@app.cell
def _(pd):
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'
    cols = ['sex', 'length', 'diam', 'height', 'weight', 'rings']
    abalone = pd.read_csv(url, usecols=[0,1,2,3,4,8], names=cols)
    return (abalone,)


@app.cell
def _(abalone):
    abalone
    return


@app.cell
def _(abalone, pd):
    abalone['ring_quartile'] = pd.qcut(abalone['rings'], q=4, labels=range(1,5))
    return


@app.cell
def _(abalone):
    grouped = abalone.groupby('ring_quartile')
    return (grouped,)


@app.cell
def _(grouped):
    grouped
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    to iterate throu the gropus:
    """)
    return


@app.cell
def _(grouped):
    for idx, frame in grouped:
        print(f'Ring Quartile: {idx}')
        print('-'* 16)
        print(frame.nlargest(3, 'weight'), end='\n\n')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    or using the getter:
    """)
    return


@app.cell
def _(grouped):
    grouped.groups.keys()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    you can access a specific group:
    """)
    return


@app.cell
def _(grouped):
    grouped.get_group(2).head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    you can use numpy functions and apply them to the group elements:
    """)
    return


@app.cell
def _(grouped):
    grouped[['height', 'weight']].agg(['mean', 'median'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Mapping Trick for Membership Binning
    """)
    return


@app.cell
def _(pd):
    countries = pd.Series([
        'United States',
        'Canada',
        'Mexico',
        'Belgium',
        'United Kingdom',
        'Thailand'
    ])

    groups = {
        'North America': ('United States', 'Canada', 'Mexico', 'Greenland'),
        'Europe': ('France', 'Germany', 'United Kingdom', 'Belgium')
    }
    return countries, groups


@app.cell
def _(groups):
    groups
    return


@app.cell
def _():
    from typing import Any

    return


@app.cell
def _(countries, groups, pd):
    def membership_map(s: pd.Series, g: dict, fillvalue=-1) -> pd.Series:
        gr = {x: k for k, v in g.items() for x in v}
        return s.map(gr).fillna(fillvalue)

    membership_map(countries, groups, fillvalue='other')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    trying returning a df:
    """)
    return


@app.cell
def _(countries, groups, pd):
    def membership_map_df(s: pd.Series, g: dict, fillvalue=-1) -> pd.DataFrame:
        gr = {x: k for k, v in g.items() for x in v}
        mapped = s.map(gr).fillna(fillvalue)
        return pd.DataFrame({
            'countries': s,
            'continents': mapped
        }).set_index('countries')

    membership_map_df(countries, groups, fillvalue='other')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How pandas Uses Boolean Operators
    """)
    return


@app.cell
def _():
    4 < 3 and 5 > 4
    return


@app.cell
def _():
    4 < (3 and 5) > 4
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    bitwise compares each elements; the logical and/or compares the truth of expression
    """)
    return


@app.cell
def _(pd):
    pd.Series([True, True, False]) & pd.Series([True, False, False])
    return


@app.cell
def _(pd):
    pd.Series([True, True, False]) and pd.Series([True, False, False])
    return


@app.cell
def _(pd):
    log_s = pd.Series(range(10))
    return (log_s,)


@app.cell
def _(log_s):
    log_s
    return


@app.cell
def _(log_s):
    log_s % 2 == 0 & log_s > 3
    return


@app.cell
def _(log_s):
    (log_s % 2 == 0) & (log_s > 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Load Data From the Clipboard
    """)
    return


@app.cell
def _(pd):
    cp = pd.read_clipboard(na_values=[], parse_dates=['d'])
    return (cp,)


@app.cell
def _(cp):
    cp
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    save data compressed to save space:
    """)
    return


@app.cell
def _(abalone):
    abalone.to_json('data.json', orient='records', lines=True)
    abalone.to_json('data.json.gz', orient='records', lines=True, compression='gzip')
    return


@app.cell
def _():
    import os
    os.path.getsize('data.json')
    return (os,)


@app.cell
def _(os):
    os.path.getsize('data.json.gz')
    return


@app.cell
def _(os):
    os.path.getsize('data.json') / os.path.getsize('data.json.gz')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## non-compressed file is 11 times bigger than compressed one!
    """)
    return


if __name__ == "__main__":
    app.run()
