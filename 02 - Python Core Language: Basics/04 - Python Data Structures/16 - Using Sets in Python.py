import marimo

__generated_with = "0.19.2"
app = marimo.App()


@app.cell
def _():
    s1 = {1, 2,(1,2), 3}
    len(s1)

    return (s1,)


@app.cell
def _():
    s2 = {1, 1, 2}
    len(s2)
    return (s2,)


@app.cell
def _(s1, s2):
    #union
    s3 = s1 | s2
    s3
    return


@app.cell
def _(s1, s2):
    s1.union(s2)
    return


@app.cell
def _():
    #intersection
    # elements that exist in all sets - inner join
    i1 = {1, 2, 3, 4}
    i2 = {2, 3, 4, 5}
    i3 = {3, 4, 5, 6}
    i4 = {4, 5, 6, 7}

    i1.intersection(i2, i3, i4)
    return i1, i2, i3, i4


@app.cell
def _(i1, i2, i3, i4):
    i1 & i2 & i3 & i4
    return


@app.cell
def _():
    # Difference
    # it's like a left join or subsctraction
    a = {1, 2, 3, 30, 300}
    b = {10, 20, 30, 40}
    c = {100, 200, 300, 400}

    a.difference(b, c)

    return


@app.cell
def _():
    #symmetric Difference
    # elements that exist in only one set but not in multiple

    sd1 = {"foo", "bar", "baz"}
    sd2 = {"baz", "qux", "quux"}

    sd1.symmetric_difference(sd2)
    return


@app.cell
def _():
    sd3 = {1, 2, 3, 4, 5}
    sd4 = {10, 2, 3, 4, 50}
    sd5 = {1, 50, 100}

    sd3 ^ sd4 ^ sd5
    return


@app.cell
def _():
    # is disjoint
    x1 = {'foo', 'bar', 'baz'}
    x2 = {'baz', 'qux', 'quux'}

    x1.isdisjoint(x2)
    return (x1,)


@app.cell
def _(x1):
    x1.isdisjoint(x1 - {'baz'})
    return


@app.cell
def _():
    #is subset
    ss1 = {1}
    ss2 = {1, 2}
    ss3 = {1, 2, 3}
    ss4 = {1, 2 ,4}

    ss1 <= ss2

    return ss1, ss2, ss3


@app.cell
def _(ss1, ss2, ss3):
    ss1 <= ss2 <= ss3
    return


@app.cell
def _(ss1, ss2, ss3):
    #proper subset

    ss1 < ss2 < ss3

    return


@app.cell
def _(ss1, ss3):
    #superset
    ss3 >= ss1
    return


@app.cell
def _(ss1, ss3):
    #is proper superset
    ss3 > ss1
    return


@app.cell
def _():
    # add, remove, discard pop and clear are simple



    return


@app.cell
def _(ss1, ss2, ss3):
    # updates:

    ss1.update(ss2) # or ss1 |= ss2

    ss1.intersection_update(ss2) # or ss1 &= ss2

    ss1.difference_update(ss2, ss3) # ss1 -= ss2 | ss3

    ss1.symmetric_difference_update(ss2) # update with elem in either sets but not multiple. ss1 ˆ= ss2



    return


app._unparsable_cell(
    r"""
    %timeit 10 * 10
    """,
    name="_"
)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
