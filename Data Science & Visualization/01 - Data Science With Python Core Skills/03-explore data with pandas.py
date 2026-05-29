import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import pandas as pd

    nba = pd.read_csv("nbaallelo.csv")
    return nba, pd


@app.cell
def _(pd):
    pd.set_option('display.max.columns', None)
    pd.set_option('display.precision', 2)
    return


@app.cell
def _(nba):
    nba.tail()
    return


@app.cell
def _(nba):
    nba.info()
    return


@app.cell
def _(nba):
    nba.describe()
    return


@app.cell
def _(nba):
    nba['matches_played'] = nba['team_id'].value_counts()
    return


@app.cell
def _(nba):
    matches_played = nba['team_id'].value_counts()
    return (matches_played,)


@app.cell
def _(matches_played, nba):
    nba['matches_played'] = nba['team_id'].map(matches_played)
    return


@app.cell
def _(nba):
    nba
    return


@app.cell
def _(matches_played):
    matches_played
    return


@app.cell
def _(nba):
    nba.loc[nba['fran_id'] == 'Lakers', 'team_id'].value_counts()
    return


@app.cell
def _(nba):
    nba.loc[nba['team_id'] == 'MNL', 'date_game'].max()
    return


@app.cell
def _(nba, pd):
    nba['date_played'] = pd.to_datetime(nba['date_game'])
    return


@app.cell
def _(nba):
    nba.loc[nba['team_id'] == 'MNL', 'date_played'].max()
    return


@app.cell
def _(nba):
    nba.info()
    return


@app.cell
def _(nba):
    total_bos_points = nba.loc[nba['team_id'] == 'BOS', 'pts'].sum()
    years_bos_played = len(nba.loc[nba['team_id'] == 'BOS', 'date_played'].apply(lambda v: v.year).unique())
    average_bos_points = total_bos_points / years_bos_played
    average_bos_points
    return


@app.cell
def _(pd):
    # exploring dataframe and Series

    revenue = pd.Series([
        555, 7000, 1980
    ])
    revenue

    return (revenue,)


@app.cell
def _(revenue):
    revenue.values
    return


@app.cell
def _(revenue):
    revenue.index
    return


@app.cell
def _(pd):
    city_revenues = pd.Series(
        [4200, 8000, 6500],
        index = ['Amsterdam', 'Toronto', 'Tokyo']
    )
    city_revenues
    return (city_revenues,)


@app.cell
def _(pd):
    city_employee_count_data = {'Amsterdam': 5, 'Tokyo': 8}
    city_employee_count = pd.Series(city_employee_count_data)
    city_employee_count
    return (city_employee_count,)


@app.cell
def _(city_employee_count):
    city_employee_count.keys()
    return


@app.cell
def _(city_employee_count):
    'Tokyo' in city_employee_count
    return


@app.cell
def _(city_employee_count, city_revenues, pd):
    city_data = pd.DataFrame({
        'revenue': city_revenues,
        'employee_count': city_employee_count
    })
    city_data
    return (city_data,)


@app.cell
def _(city_data):
    city_data.axes
    return


@app.cell
def _(pd):
    #accessing data in a Series
    colors = pd.Series(
        ['red','purple','blue','green','yellow'],
        index = [1, 2, 3, 5, 8]
    )
    colors

    return (colors,)


@app.cell
def _(colors):
    colors[1]
    return


@app.cell
def _(colors):
    colors.loc[1]
    return


@app.cell
def _(colors):
    colors.iloc[1]
    return


@app.cell
def _(city_data):
    #Accessing data in a DataFrame

    city_data.loc['Amsterdam']
    return


@app.cell
def _(city_data):
    city_data.iloc[1]
    return


@app.cell
def _(city_data):
    # slicing
    city_data.loc['Tokyo': 'Toronto']
    return


@app.cell
def _(nba):
    nba.loc[5555:5559, ['fran_id', 'opp_fran', 'pts', 'opp_pts']]
    return


@app.cell
def _(nba):
    #querying data

    current_dacade = nba[nba['year_id'] > 2010]
    current_dacade
    return


@app.cell
def _(nba):
    nba['notes'].notnull().count()
    return


@app.cell
def _(nba):
    ers_team = nba.loc[nba['fran_id'].str.endswith('ers'), 'fran_id'].value_counts()
    ers_team
    return


@app.cell
def _(nba):
    nba[(nba['team_id'] == 'BLB') & (nba['pts'] > 100) & (nba['opp_pts'] > 100)]
    return


@app.cell
def _(city_revenues):
    # grouping

    city_revenues.sum()
    return


@app.cell
def _(city_revenues):
    city_revenues.min()
    return


@app.cell
def _(nba):
    nba['fran_id'].unique()
    return


@app.cell
def _(nba):
    group_fran = nba.groupby('fran_id', sort=False)
    group_fran
    return (group_fran,)


@app.cell
def _(group_fran):
    group_fran['pts'].sum()
    return


@app.cell
def _(nba):
    nba[['year_id', 'game_result']]
    return


@app.cell
def _(nba):
    year_results = nba[nba['fran_id'] == 'Bulls'].groupby(['year_id', 'game_result'])['game_id'].count()
    year_results
    return


@app.cell
def _(nba):
    nba[
        (nba['fran_id'] == 'Warriors') &
        (nba['year_id'] == 2015)
    ].groupby(['is_playoffs', 'game_result'])['game_id'].count()
    return


@app.cell
def _(nba):
    nba_copy = nba.copy()
    return (nba_copy,)


@app.cell
def _(nba, nba_copy):
    nba_copy['difference'] = nba['pts'] - nba['opp_pts']
    nba_copy
    return


@app.cell
def _(nba_copy):
    nba_copy['difference'].max()
    return


@app.cell
def _(nba_copy):
    nba_copy.rename(
        columns={
            'game_location': 'location',
            'game_result' : 'result'
        }
    )
    return


@app.cell
def _(nba_copy):
    elo_columns = ['elo_i', 'elo_n', 'opp_elo_i', 'opp_elo_n']
    nba_copy.drop(elo_columns, axis=1, inplace=True)
    nba_copy
    return


@app.cell
def _(nba_copy):
    # Clean Data
    # dropna method drops any row with NAs, so we can use drop(axis=1) to drop columns

    nba_copy.dropna(axis=1) # so we drop only 'notes' column
    nba_copy.shape
    return


@app.cell
def _(nba_copy):
    nba_copy.fillna({
        'notes': 'no notes at all'
    }, inplace=True
    )

    return


@app.cell
def _(city_data):
    #combine multi dataframes

    city_data
    return


@app.cell
def _(pd):
    further_city_date = pd.DataFrame(
        {
            'revenue': [7000, 3400],
            'employee_count': [2, 2]
        },
        index = ['New York', 'Barcelona']
    )
    return (further_city_date,)


@app.cell
def _(city_data, further_city_date, pd):
    all_city_data = pd.concat([city_data, further_city_date], sort=False)
    all_city_data
    return (all_city_data,)


@app.cell
def _(pd):
    city_countries = pd.DataFrame({
        'country': ['holland', 'Japan', 'Holland', 'Canada', 'Spain'],
        'capital': [1, 1, 0, 0, 0]
    }, index = ['Amsterdam', 'Tokyo', 'Rotterdam', 'Toronto', 'Barcelona']
    )
    return (city_countries,)


@app.cell
def _(all_city_data, city_countries, pd):
    cities = pd.concat([all_city_data, city_countries], axis=1, sort=False, join='inner')
    cities
    return (cities,)


@app.cell
def _(pd):
    countries = pd.DataFrame({
        'population_millions': [17, 127, 37],
        'continent': ['Europe', 'Asia', 'North America']
    }, index=['Holland', 'Japan', 'Canada'])
    return (countries,)


@app.cell
def _(cities, countries, pd):
    # How to merge a column with the index of the other DataFrame:

    pd.merge(cities, countries, left_on='country', right_index=True)
    return


@app.cell
def _(cities, countries, pd):
    #using left join;

    pd.merge(cities, countries, left_on='country', right_index=True, how='left')
    return


@app.cell
def _(nba):
    #visualizations

    knicks_pts_by_year = nba[nba['fran_id'] == 'Knicks'].groupby('year_id')['pts'].sum()
    knicks_pts_by_year
    return (knicks_pts_by_year,)


@app.cell
def _(knicks_pts_by_year):
    knicks_pts_by_year.plot()
    return


@app.cell
def _(knicks_pts_by_year):
    knicks_pts_by_year.tail(20).plot(kind='bar')
    return


@app.cell
def _(nba):
    nba[(nba['fran_id'] == 'Knicks') & (nba['year_id'] > 2000)].plot(kind='scatter', x='pts', y='opp_pts', s=0.5)
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
