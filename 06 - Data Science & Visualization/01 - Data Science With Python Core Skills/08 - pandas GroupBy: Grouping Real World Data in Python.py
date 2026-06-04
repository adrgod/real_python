import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # pandas GroupBy: Grouping Real World Data in Python
    """)
    return


@app.cell
def _():
    from IPython.utils.jsonutil import parse_date
    import pandas as pd

    legis_dtype = {
        'first_name': 'category',
        'gender': 'category',
        'type': 'category',
        'state': 'category',
        'party': 'category'
    }

    legislators_data = pd.read_csv(
        './data-sets/legislators-historical.csv',
        dtype=legis_dtype,
        usecols= list(legis_dtype) + ['birthday', 'last_name'],
        parse_dates=['birthday']
        )

    legislators_data.head(5)
    return legislators_data, pd


@app.cell
def _(legislators_data):
    legislators_data.info()
    return


@app.cell
def _(legislators_data):
    legislators_data.groupby('state')['last_name'].count()
    return


@app.cell
def _(legislators_data):
    count_by_state = legislators_data.groupby('state')['last_name'].count()
    return (count_by_state,)


@app.cell
def _(count_by_state):
    count_by_state
    return


@app.cell
def _(legislators_data):
    legislators_data.groupby(['state', 'gender'])['last_name'].count().head(10)
    return


@app.cell
def _(legislators_data):
    n_by_state_gender = legislators_data.groupby(['state', 'gender'])['last_name'].count().head(10)
    return (n_by_state_gender,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    the type return is not a dataframe - it's a series. the index of this 2-columns series in a coumpound index
    """)
    return


@app.cell
def _(n_by_state_gender):
    type(n_by_state_gender)
    return


@app.cell
def _(n_by_state_gender):
    n_by_state_gender.index
    return


@app.cell
def _(legislators_data):
    legislators_data.groupby(['state', 'gender'], as_index=True)['last_name'].count().head(10)
    #as_index doens't work here in marimo, or new pandas version maybe
    return


@app.cell
def _(pd):
    orders = pd.DataFrame({
         "location": ["Downtown", "Airport", "Downtown", "Mall"],
         "price": [4.50, 3.25, 5.00, 2.75],
    })

    return (orders,)


@app.cell
def _(orders):
    orders
    return


@app.cell
def _(orders):
    type(orders.groupby('location')['price'].sum())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Split/Combine/Apply
    """)
    return


@app.cell
def _(legislators_data):
    by_state = legislators_data.groupby('state')
    return (by_state,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    this returns a group name, 'state; in this case. and a dataframe with the rest of the fields
    """)
    return


@app.cell
def _(by_state):
    for state, frame in by_state:
        print(f'--- First 2 entries for {state!r}')
        print(frame.head(2), end='\n\n')
    return


@app.cell
def _(by_state):
    by_state.groups['PA']
    return


@app.cell
def _(by_state):
    by_state.get_group('PA')
    # this is the same as legislators_date.loc[legislators['state'] == 'PA']
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What the FOR loolp is doing is iteration through the items of the dataframe, similar to t, we can do:
    """)
    return


@app.cell
def _(by_state):
    next_state, next_frame = next(iter(by_state))
    return next_frame, next_state


@app.cell
def _(next_state):
    next_state
    return


@app.cell
def _(next_frame):
    next_frame
    return


@app.cell
def _(next_frame):
    type(next_frame)
    #the frame is a dataframe
    return


@app.cell
def _(next_frame):
    next_frame['last_name']
    return


@app.cell
def _(next_frame):
    next_frame['last_name'].count()
    return


@app.cell
def _(legislators_data):
    legislators_data.groupby('state')['last_name'].count().head(1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## exercice:
    """)
    return


@app.cell
def _(pd):
    drink_orders = pd.DataFrame({
        "location": ["Downtown", "Downtown", "Downtown",
        "Airport", "Airport", "Airport", "Airport"],
        "drink_type": ["Latte", "Latte", "Espresso",
            "Latte", "Latte", "Espresso", "Cold Brew"],
        "price": [4.50, 5.00, 3.00, 5.00, 5.50, 3.50, 5.00],
    })
    return (drink_orders,)


@app.cell
def _(drink_orders):
    drink_orders.groupby(['location', 'drink_type'])['price'].mean().reset_index()
    return


@app.cell
def _(pd):


    air = pd.read_csv(
        'data-sets/airqual.csv',
        na_values = [-200],
        usecols = ['Date', 'Time', 'CO(GT)', 'T', 'RH', 'AH']
    )

    return (air,)


@app.cell
def _(air):
    air
    return


@app.cell
def _(air, pd):
    air['tstamp'] = pd.to_datetime(air.pop('Date') + ' ' + air.pop('Time'),
    format = '%m/%d/%y %H:%M:%S')
    return


@app.cell
def _(air):
    air
    return


@app.cell
def _(air):
    air.rename(columns={
        'CO(GT)': 'co',
        'T': 'temp_c',
        'RH': 'rel_hum',
        'AH': 'abs_hum',
    }, inplace=True)

    air.set_index('tstamp', inplace=True)

    air
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    now, let's create a series with the days of the week of each of those days
    """)
    return


@app.cell
def _(air):
    day_names = air.index.day_name()
    return (day_names,)


@app.cell
def _(day_names):
    type(day_names)
    # the returned is an index
    return


@app.cell
def _(air, day_names):
    # and because it's an index we can use it to access it a perform a groupby
    air.groupby(day_names)['co'].mean()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    let's do the same for hour now:
    """)
    return


@app.cell
def _(air):
    day_hour = air.index.hour
    return (day_hour,)


@app.cell
def _(air, day_hour):
    air.groupby(day_hour)['co'].mean()
    return


@app.cell
def _(air, day_hour, day_names):
    # or by day/hour:
    air.groupby([day_names, day_hour])['co'].mean()
    return


@app.cell
def _(air, day_hour, day_names):
    air.groupby([day_names, day_hour])['co'].mean().rename_axis(['weekday', 'hour'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bins
    """)
    return


@app.cell
def _(air, pd):
    bins = pd.cut(air['temp_c'], bins=3, labels = ('cool', 'warm', 'hot'))
    return (bins,)


@app.cell
def _(bins):
    bins
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    this returns a series with the same index, of course. so we can use it to use those groups in the dataframe for calculations on other numeric values
    """)
    return


@app.cell
def _(air, bins):
    air[['rel_hum', 'abs_hum']].groupby(bins).agg(['mean', 'median'])
    return


@app.cell
def _(air):
    air.groupby([air.index.year, air.index.quarter])['co'].agg(['max', 'min']).rename_axis(['year', 'quarter'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Because the index is a time series, we can do the same thing but using resample:
    """)
    return


@app.cell
def _(air):
    air.resample('QE')['co'].agg(['max', 'min'])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Excercise:
    """)
    return


@app.cell
def _(pd):
    coffee_timestamps = pd.to_datetime([
         "2024-06-03 08:15",  # Monday
         "2024-06-03 10:00",  # Monday
         "2024-06-04 09:00",  # Tuesday
         "2024-06-05 11:30",  # Wednesday
         "2024-06-05 14:00",  # Wednesday
     ])

    coffee_orders = pd.DataFrame(
        {"price": [4.50, 3.25, 5.00, 2.75, 4.50]},
        index=coffee_timestamps,
     ).rename_axis('time')

    coffee_orders
    return (coffee_orders,)


@app.cell
def _(coffee_orders):
    coffee_week_days = coffee_orders.index.day_name()
    return (coffee_week_days,)


@app.cell
def _(coffee_orders, coffee_week_days):
    coffee_orders.groupby(coffee_week_days)['price'].count()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Lambdas
    """)
    return


@app.cell
def _(pd):
    news = pd.read_csv(
        'data-sets/news.csv',
        sep='\t',
        index_col=0,
        names=['title', 'url', 'outlet', 'category', 'cluster', 'host', 'tstamp'],
        dtype={
            'outlet': 'category',
            'category': 'category',
            'cluster': 'category',
            'host': 'category',
        },
    )

    news['tstamp'] = pd.to_datetime(news['tstamp'], unit='ms')

    return (news,)


@app.cell
def _(news):
    news.head(10)
    return


@app.cell
def _(news):
    news.groupby('outlet', sort=False)['title'].apply( # and apply applies all the counts of Trues for each outlet
        lambda ser: ser.str.contains('Fed').sum() # -> because the contains test returns a series with booleans, a sum will count how many are True!!
    ).nlargest(10) # and we show top 10
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using lambda makes lambda to use python, so it's slower.
    Same calculation using only pandas:
    """)
    return


@app.cell
def _(news):
    mentions_fed = news['title'].str.contains('Fed')
    return (mentions_fed,)


@app.cell
def _(mentions_fed):
    mentions_fed
    return


@app.cell
def _(mentions_fed, news):
    mentions_fed.groupby(news['outlet']).sum().nlargest(10)
    return


@app.cell
def _(mentions_fed, news):
    import numpy as np
    mentions_fed.groupby(news['outlet']).sum().nlargest(10).astype(np.uintc)

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
