import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Combining Data in pandas With concat() and merge()
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Concat()
    """)
    return


@app.cell
def _():
    import pandas as pd

    orchard = [
        {'name': 'apple', 'image': 'a'},
        {'name': 'pear', 'image': 'p'},
        {'name': 'tomato', 'image': 't'},
        {'name': 'lemon', 'image': 'l'}
    ]

    garden = [
        {'name': 'tomato', 'color': 'red', 'image': 't'},
        {'name': 'potato', 'color': 'browm', 'image': 'p'},
        {'name': 'carrot', 'color': 'orange', 'image': 'c'}
    ]

    fruits =  pd.DataFrame(orchard)
    veggies = pd.DataFrame(garden)

    return fruits, pd, veggies


@app.cell
def _(fruits, pd, veggies):
    pd.concat([fruits, veggies])
    return


@app.cell
def _(fruits, pd, veggies):
    pd.concat([fruits, veggies], axis='columns')
    return


@app.cell
def _(fruits, pd, veggies):
    pd.concat([fruits, veggies], axis='columns', keys=['fruits', 'veggies'])
    return


@app.cell
def _(fruits, pd, veggies):
    single = pd.concat([fruits, veggies])
    return (single,)


@app.cell
def _(single):
    single.loc[1:2,:] #doesn't work
    return


@app.cell
def _(single):
    single.iloc[1:2,:]
    return


@app.cell
def _(fruits, pd, veggies):
    multivitamin = pd.concat([fruits, veggies], keys=['fruits', 'veggies'])
    # this creates a multi-index
    return (multivitamin,)


@app.cell
def _(multivitamin):
    multivitamin
    return


@app.cell
def _(multivitamin):
    multivitamin.loc[('fruits', 1):('fruits', 2),:]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ignore index:
    """)
    return


@app.cell
def _(fruits, pd, veggies):
    pd.concat([fruits, veggies], ignore_index=True).reset_index()
    return


@app.cell
def _(fruits, pd, veggies):
    pd.concat([fruits, veggies], axis='rows', join='outer')
    return


@app.cell
def _(fruits, pd, veggies):
    pd.concat([fruits, veggies], axis='rows', join='inner')
    #this removed columns where there are NANs
    return


@app.cell
def _(fruits, pd, veggies):
    pd.concat([fruits, veggies], axis='columns', join='inner')
    return


@app.cell
def _(fruits, pd, veggies):
    pd.concat([fruits, veggies], axis='rows', join='outer')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    with merge, it tries to join matching values together:
    """)
    return


@app.cell
def _(fruits, pd, veggies):
    pd.merge(fruits, veggies)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    the right merge is the same as a sql right join
    """)
    return


@app.cell
def _(fruits, pd, veggies):
    pd.merge(fruits, veggies, how ='right')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    when we specify the on= column, and we use a subset of the matching columns in both dataframes - pandas will output all matching columns not used in on= parameter:
    """)
    return


@app.cell
def _(fruits, pd, veggies):
    pd.merge(fruits, veggies, on='name')
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
