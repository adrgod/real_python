import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    # use in and not find or index, because of simplicity

    # regex
    import re

    text = "bla bla bla secret, secret. Secret and SECRET."

    m = re.search(r"secret", text)
    print(m)

    return re, text


@app.cell
def _(re, text):
    m_all = re.findall(r"secret", text)
    print(m_all)
    return


@app.cell
def _(re, text):
    #using parentisis makes the return change, even tho the match is using secret.
    m_part = re.findall(r"secre(t[\.,])", text)
    print(m_part)
    return


@app.cell
def _(re, text):
    #or returning a tuple of the word part match, and the punctuation:

    m_tuple = re.findall(r"(secret)([\.,])", text)
    print(m_tuple)
    return


@app.cell
def _(re, text):
    #to find all and have the range info, use finditer:

    for f in re.finditer(r"secret[\.,]", text):
        print(f)
    return


@app.cell
def _(re, text):
    #using group to display:

    for mg in re.finditer(r"(secret)([\.,])", text):
        print(mg.group(1), mg.span(), mg.group(2))
    return


@app.cell
def _():
    #working with pandas

    import pandas as pd

    companies =pd.read_csv("./companies.csv")
    companies.shape
    companies.head()
    return (companies,)


@app.cell
def _(companies):
    #to return the boolean value of the test:

    companies.slogan.str.contains("secret")
    return


@app.cell
def _(companies):
    # to filter:

    companies[companies.slogan.str.contains("secret")]
    return


@app.cell
def _(companies):
    #to filter with regex:

    companies[companies.slogan.str.contains(r"secret\w+")]
    return


if __name__ == "__main__":
    app.run()
