import marimo

__generated_with = "0.19.2"
app = marimo.App()


@app.cell
def _():
    integers = [1, 2, 8, 15,16, 24, 42, 50, 63, 78, 81, 90, 100]
    return (integers,)


@app.cell
def _(integers):
    for number in integers:
        print(number)
    return


@app.cell
def _(integers):
    for i, n in enumerate(integers):
        print(f"Index {i}: {n}")
    return


@app.cell
def _():
    numbers = [-10, 4, -7, 5, 9]
    return (numbers,)


@app.cell
def _(numbers):
    [abs(number) for number in numbers]
    return


@app.cell
def _(numbers):
    absolutes = list(map(abs, numbers))
    absolutes
    return


@app.cell
def _(numbers):
    positives = list(filter(lambda number: number >=0, numbers))
    positives
    return


@app.cell
def _(numbers):
    odd_ones = list(map(lambda x: x%2 != 0, numbers))
    odd_ones

    return


@app.cell
def _():
    #return index of all occurrences of an element in a list
    elems = [1, 7, -2, 9, 7, 3, 7]

    def number_indexes(elem, lst):
        return [i for i, n in enumerate(lst) if n == elem]

    number_indexes(-2, elems)

    return


if __name__ == "__main__":
    app.run()
