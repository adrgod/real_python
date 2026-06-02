import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd

    df = pd.DataFrame({
        'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
        'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
                 'Manchester', 'Cairo', 'Osaka'],
        'age': [41, 28, 33, 34, 38, 31, 37],
        'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
    }, index= range(101, 108)
    )
    df.reset_index()
    return df, pd


@app.cell
def _(mo):
    mo.md(r"""
    ## Creating a pandas DataFrame
    """)
    return


@app.cell
def _():
    import numpy as np
    d = {'x': [1,2,3], 'y': np.array([2,4,8]), 'z': 100}
    return d, np


@app.cell
def _(d, pd):
    pd.DataFrame(d, index = [100, 200, 300], columns=['x', 'y', 'z'])
    return


@app.cell
def _(pd):
    lst = [{"x": 1, "y": 2, "z": 100},
           {"x": 2, "y": 4, "z": 100},
           {"x": 3, "y": 8, "z": 100}]
    pd.DataFrame(lst, index=['a', 'b', 'c'])
    return


@app.cell
def _():
    lst2 = [[1, 2, 100],
            [2, 4, 100],
            [3, 8, 100]]
    return (lst2,)


@app.cell
def _(lst2, pd):
    pd.DataFrame(lst2).reset_index()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    npArray based DataFrame stays linked to npArray - changes to a value in npArray will be reflected in df
    """)
    return


@app.cell
def _(np, pd):
    arr = np.array([[1, 2, 100],
            [2, 4, 100],
            [3, 8, 100]])
    df_ = pd.DataFrame(arr, columns = ['x', 'y', 'z'], copy=False)

    return arr, df_


@app.cell
def _(df_):
    df_
    return


@app.cell
def _(arr):
    arr[1,1] = 33
    return


@app.cell
def _(df_):
    df_
    return


@app.cell
def _(df):
    df.dtypes
    return


@app.cell
def _(df, np):
    df__ = df.astype(dtype={'age': np.int16, 'py-score': np.float32})
    return (df__,)


@app.cell
def _(df__):
    df__.dtypes
    return


@app.cell
def _(df__):
    df__.size
    return


@app.cell
def _(df__):
    df__.shape
    return


@app.cell
def _(df__):
    df__.memory_usage()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Modifying Data in DataFrame
    """)
    return


@app.cell
def _(df):
    df['name']
    return


@app.cell
def _(df):
    df.name
    return


@app.cell
def _(df):
    df.index
    return


@app.cell
def _(df):
    df.loc[101]
    return


@app.cell
def _(df):
    df.loc[[101,104], ['name', 'city']]
    return


@app.cell
def _(df):
    df.loc[[x for x in df.index if x % 2]].reset_index()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## iLoc Method
    """)
    return


@app.cell
def _(df):
    df.iloc[0, [0,2]]
    return


@app.cell
def _(df):
    df.iloc[:, [0,2]]
    return


@app.cell
def _(df):
    df.at[102, 'city']
    return


@app.cell
def _(df):
    df.iat[2,1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Changing Values
    """)
    return


@app.cell
def _(df):
    df.loc[:104, ['py-score']] = [40, 50, 60, 70]
    df.loc[105:, ['py-score']] = 0
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df, np):
    df.iloc[:, -1] = np.linspace(20, 50, len(df))
    df
    return


@app.cell
def _(df, pd):
    john = pd.Series(data=['John', 'Vila Verde', 27, 80], index=df.columns, name=108)
    john
    return (john,)


@app.cell
def _(df, john, pd):
    df1 = pd.concat([df, pd.DataFrame([john])], ignore_index=False)
    return


@app.cell
def _(df):
    df.drop(labels=[7,8,9,10], inplace=True)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df.insert(loc=4, column='django-score', value=[50, 60, 70, 80, 90, 60, 70])
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    del df['django-score']
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    #drop column with method drop:

    df.drop(labels=['age'], axis=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Arithmetic operations
    """)
    return


@app.cell
def _(df):
    df['py-score'] * 2
    return


@app.cell
def _(df):
    df['age'] = [41,
    28,
    33,
    34,
    38,
    31,
    37]
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['age'] + df['py-score']
    return


@app.cell
def _(df):
    df['django-score'] = [50, 60, 70, 80, 90, 60, 70]
    df['js-score'] = [65, 85, 75, 63, 86, 68, 79]
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['total-score'] = 0.4 * df['py-score'] + 0.3 * df['django-score'] + 0.3 * df['js-score']
    df
    return


@app.cell
def _(pd):
    wgts = pd.Series(data=[0.4, 0.3, 0.3], index=['py-score', 'django-score', 'js-score'])
    return (wgts,)


@app.cell
def _(df, np, wgts):
    np.sum(df[wgts.index] * wgts, axis=1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sorting
    """)
    return


@app.cell
def _(df):
    df.sort_values('js-score', ascending=False)
    return


@app.cell
def _(df):
    df.sort_values(by=['js-score', 'py-score'], ascending=[False, False])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Filtering with Operators
    """)
    return


@app.cell
def _(df):
    df['py-score'] > 40
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    this creates a series, which result can be used to filter on a df..
    """)
    return


@app.cell
def _(df):
    filter_ = (df['py-score'] >= 40) | (df['js-score'] >= 70)
    df[filter_]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Filter using .where() and .filter()
    """)
    return


@app.cell
def _(df):
    df['js-score'].where(cond=df['js-score'] >= 80, other=0.0)
    return


@app.cell
def _(df):
    df.filter(items=['py-score', 'js-score', 'django-score'])
    return


@app.cell
def _(df):
    df.filter(regex='score')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## NaN values
    """)
    return


@app.cell
def _(np, pd):
    df_nan = pd.DataFrame({'x': [1,2,np.nan,4]})
    df_nan
    return (df_nan,)


@app.cell
def _(df_nan):
    df_nan.fillna(value=0)
    return


@app.cell
def _(df_nan):
    df_nan.mean()
    return


@app.cell
def _(df_nan):
    df_nan.fillna(value=0).mean()
    return


@app.cell
def _(df_nan):
    df_nan.bfill()
    return


@app.cell
def _(df_nan):
    df_nan.interpolate('linear')
    return


@app.cell
def _(df_nan):
    df_nan.dropna()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Iterate over Rows or Columns
    """)
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    col_label, col = next(df.items())
    return col, col_label


@app.cell
def _(col_label):
    col_label
    return


@app.cell
def _(col):
    col
    return


@app.cell
def _(df):
    for column_label, col_data in df.items():
        print(column_label, col_data, sep='\n', end='\n\n')
    return


@app.cell
def _(df):
    for row_label, row in df.iterrows():
        print(row_label, row, sep='\n', end='\n\n')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Itertuples return Named Tuples
    """)
    return


@app.cell
def _(df):
    for itpl in df.itertuples():
        print(f"Name: {itpl.name}, City: {itpl.city}")
    return


@app.cell
def _(df):
    for itpl2 in df.itertuples(index=False, name='JobCandidate'):
        print(itpl2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Time-Series in Pandas
    """)
    return


@app.cell
def _():
    temp_c = [ 8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0,
               9.1, 12.8, 15.3, 19.1, 21.2, 22.1, 22.4, 23.1,
              21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]
    return (temp_c,)


@app.cell
def _(pd):
    dt = pd.date_range(start='2019-10-27 00:00:00', periods=24, freq='h')
    return (dt,)


@app.cell
def _(dt, pd, temp_c):
    temp = pd.DataFrame(data={'temp_c': temp_c}, index=dt)
    return (temp,)


@app.cell
def _(temp):
    temp
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Slicing the time-series
    """)
    return


@app.cell
def _(temp):
    temp['2019-10-27 05': '2019-10-27 15']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Resamplig:
    """)
    return


@app.cell
def _(temp):
    temp.resample(rule='6h').mean()
    return


@app.cell
def _(temp):
    temp.rolling(window=3, center=True).mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Plot!
    """)
    return


@app.cell
def _(temp):
    temp.plot()
    return


@app.cell
def _(temp):
    temp.plot(kind='line', color='g', style='.-', mfc='k', ms=10)
    return


@app.cell
def _(temp):
    temp.plot(kind='line', color='g', style='.-', mfc='k', ms=10).get_figure().savefig('temps.png')
    return


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    df['py-score'].plot.hist(bins=5, alpha=0.8)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
