import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _(mo):
    mo.md(r"""
    # Data Cleaning With pandas and NumPy
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Olympics
    """)
    return


@app.cell
def _():
    import pandas as pd

    def read_ol():
        data = pd.read_csv('./data-sets/olympics.csv', header=1).rename(columns={
            'Unnamed: 0': 'country',

        })
        return data

    olympics = read_ol()
    olympics.head(5).reset_index()
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Booleans to select elements in DataFrame
    """)
    return


@app.cell
def _(pd):
    dates = pd.DataFrame([
        [1,1,2000],
        [12,12,1999]
    ], columns=['day', 'month', 'year'])
    dates
    return (dates,)


@app.cell
def _(pd):
    col_dates = pd.DataFrame({
        'day': [1, 12],
        'month': [1,12],
        'year': [2000, 1999]
    })
    col_dates
    return


@app.cell
def _(dates):
    dates.loc[[True, False]]
    return


@app.cell
def _(dates):
    dates.loc[[False, True], [True, False, True]]
    return


@app.cell
def _(dates):
    dates[dates.loc[:, 'day'] > 5]
    return


@app.cell
def _(dates):
    dates.loc[[False, True]]
    dates.index.name = 'id'
    dates
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercice is:
    """)
    return


@app.cell
def _(pd):
    ex1 = pd.DataFrame({
        "country": ["USA", "Canada", "Germany", "Brazil"],
        "gold": [1022, 64, 150, 30],
        "silver": [795, 102, 160, 40],
        "bronze": [705, 65, 180, 50],
        "total": [2522, 231, 490, 120],
    })

    #get_top_countries(df, 100)
    #   country  total
    #0      USA   2522
    #2  Germany    490

    return (ex1,)


@app.function
def get_top_countries(df, min_gold):
    """Filter countries by gold medal count."""
    return df.loc[df['gold'] > min_gold, ['country', 'total']]


@app.cell
def _(ex1):
    get_top_countries(ex1, 100)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## University Dataset
    """)
    return


@app.cell
def _(pd):
    def read_universities():
        towns = []
        state = ""
        with open('./data-sets/university_towns.txt', mode='r') as f:
            for line in f:
                if "[edit]" in line:
                    state = line.strip()
                else:
                    towns.append([state, line])
        return pd.DataFrame(towns, columns=['state', 'towns'])


    towns = read_universities()
    towns.to_csv('towns.csv')

    return (towns,)


@app.cell
def _(towns):
    towns.loc[:, 'state'].str.contains("\[edit\]").all()
    return


@app.cell
def _(pd):
    clean_towns = pd.read_csv('towns.csv', index_col=0).assign(
        state=lambda df: df.loc[:,'state'].str.removesuffix("[edit]"),
        towns=lambda df: df.loc[:,'towns'].str.extract(r"(.+) \(.*")
    )
    clean_towns
    return


@app.cell
def _(dates):
    dates
    return


@app.cell
def _(dates):
    dates.assign(
        day=lambda df: df.loc[:,'day'],
        month=lambda df: df.loc[:,'month']
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Books Data
    """)
    return


@app.cell
def _(pd):
    def read_books():
        return (
            pd.read_csv("data-sets/BL-Flickr-Images-Book.csv")
            .rename(columns=lambda header: header.lower().replace(" ", "_"))
            .rename(columns={'identifier': 'id'})
            .drop(columns=[
                'edition_statement', 
                'contributors',
                'corporate_author', 
                'corporate_contributors', 
                'former_owner',
                'engraver', 
                'issuance_type', 
                'shelfmarks'
                ]
            )
            .set_index('id')
        )

    books = read_books()
    books
    return (books,)


@app.cell
def _(books):
    books.loc[:,'id'].is_unique
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cleaning Date Columns
    """)
    return


@app.cell
def _(books):
    books.loc[:, 'date_of_publication'].str.extract(
        r"(\d{4})",
        expand=False #otherwise extract return a DataFrame. we need a Series.
    ).fillna(0)
    return


@app.cell
def _(books, pd):
    #we need to make year as a numeric value
    pd.to_numeric(
        books.loc[:, 'date_of_publication'].str.extract(
        r"(\d{4})",
        expand=False #otherwise extract return a DataFrame. we need a Series.
    ).fillna(0),
    downcast='unsigned'
    )
    return


@app.cell
def _(pd):
    def clean_date_of_publication(books):
     return pd.to_numeric(
            books.loc[:, 'date_of_publication'].str.extract(
            r"(\d{4})",
            expand=False #otherwise extract return a DataFrame. we need a Series.
        ).fillna(0),
        downcast='unsigned'
        )

    return (clean_date_of_publication,)


@app.cell
def _(clean_date_of_publication, pd):
    def read_books_clean():
        return (
            pd.read_csv("data-sets/BL-Flickr-Images-Book.csv")
            .rename(columns=lambda header: header.lower().replace(" ", "_"))
            .rename(columns={'identifier': 'id'})
            .drop(columns=[
                'edition_statement', 
                'contributors',
                'corporate_author', 
                'corporate_contributors', 
                'former_owner',
                'engraver', 
                'issuance_type', 
                'shelfmarks'
                ]
            )
            .set_index('id')
            .assign(date_of_publication=clean_date_of_publication)
        )

    books_clean = read_books_clean()
    books_clean
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Clean Place of Publication
    """)
    return


@app.cell
def _(books):
    books.loc[books.loc[:, 'place_of_publication'].str.contains('-'), 'place_of_publication']
    return


@app.cell
def _(books):
    def clean_place_of_publication(books):
        return (
            books.loc[:, 'place_of_publication']
            .str.replace(r"(.*London.*)", "London", regex=True)
            .str.replace('-', ' ', regex=True)
        )

    clean_place_of_publication(books)
    return (clean_place_of_publication,)


@app.cell
def _(clean_date_of_publication, clean_place_of_publication, pd):
    def read_books_clean_place():
        return (
            pd.read_csv("data-sets/BL-Flickr-Images-Book.csv")
            .rename(columns=lambda header: header.lower().replace(" ", "_"))
            .rename(columns={'identifier': 'id'})
            .drop(columns=[
                'edition_statement', 
                'contributors',
                'corporate_author', 
                'corporate_contributors', 
                'former_owner',
                'engraver', 
                'issuance_type', 
                'shelfmarks'
                ]
            )
            .set_index('id')
            .assign(date_of_publication=clean_date_of_publication,
            place_of_publication=clean_place_of_publication)
        )

    books_clean_place = read_books_clean_place()
    books_clean_place
    return


@app.cell
def _(pd):
    test_books = pd.DataFrame({
        "Book Title": ["Great Expectations"],
        "Date Of Publication": [1861],
        "Place Of Publication": ["London"],
        "Flickr URL": ["http://example.com"],
    })

    def clean_dataframe(df, to_drop):
        """Rename columns to snake_case and drop unwanted ones."""
        return df.rename(columns=lambda header: header.lower().replace(" ","-"))

    clean_dataframe(test_books, to_drop=["flickr_url"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## TODO: read year from place of publication, when year of publication is empty
    """)
    return


if __name__ == "__main__":
    app.run()
