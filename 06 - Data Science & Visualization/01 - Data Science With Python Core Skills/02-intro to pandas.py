import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import requests

    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    headers = {"User-Agent": ""}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print("HTTP status:", response.status_code)
    return (response,)


@app.cell
def _(response):
    import pandas as pd
    from io import StringIO

    html = response.text
    print("HTML length:", len(html))
    if not html.strip():
        raise RuntimeError("Empty HTML response")

    tables = pd.read_html(StringIO(html))
    print(tables)
    return (tables,)


@app.cell
def _(tables):
    tables[0]
    return


@app.cell
def _(tables):
    tables[0].to_csv("world_population.csv")
    return


@app.cell
def _(tables):
    data = tables[0]
    return (data,)


@app.cell
def _(data):
    type(data)
    return


@app.cell
def _(data):
    data["Population"].drop(0).mean()
    return


@app.cell
def _(data):
    data["Population"].drop(0).median()
    return


if __name__ == "__main__":
    app.run()
