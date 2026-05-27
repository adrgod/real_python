import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    #iterate through list

    squares: list[int]= []

    for i in range(10):
        squares.append(i* i)

    print(squares)

    return


@app.cell
def _():
    #using map
    net_values = [1.09, 23.56, 57.84, 6.78]

    TX_RATE = 0.08

    def add_tx(val: float) -> float:
        return round(val * (1 + TX_RATE), 4)

    values_with_taxes = map(add_tx, net_values)

    list(values_with_taxes)
    return add_tx, net_values


@app.cell
def _(add_tx, net_values):
    #and finally with a list comprehension

    gross_values = [add_tx(val) for val in net_values]
    print(gross_values)
    return


@app.cell
def _():
    #with filters now

    transcription = "00:00 In order to understand the full value that list comprehensions can provide, it’s helpful to understand their range of possible functionality. You’ll also want to understand the changes that were made to list comprehension in Python 3.8, so we’ll cover these also. Firstly, let’s look at using conditional logic. In the previous lesson, you saw this formula for how to create list comprehensions. While this formula is accurate, it’s also a bit incomplete."

    def is_consonant(letter):
        vowels = 'aeiou'
        return letter.isalpha() and letter.lower() not in vowels

    #this filters out elements:
    consonants = [l for l in transcription if is_consonant(l)]
    print(consonants)

    return (transcription,)


@app.cell
def _():
    #this doesn't filter, it iterates through all elements but 
    # applies function to elements that respect the logical validation

    original_prices = [1.25, -9.45, 10.22, -3.50, 12.20, -6.30]

    fixed_prices = [price if price >= 0 else 0 for price in original_prices]
    print(fixed_prices)
    return


@app.cell
def _(transcription):
    # can work with sets (and dicts)

    unique_vowels = {l.lower() for l in transcription}
    print(unique_vowels)
    return


@app.cell
def _():
    #storing output of conditional call to function, to use it in comprehension (wow)

    import random
    def get_weather_data():
        return random.randrange(90,110)

    # here we assign temp to a value that is compared to 100 and returned if condition is met.
    hot_temp = [ temp for _ in range(10) if (temp := get_weather_data()) >= 100]

    print(hot_temp)
    return


if __name__ == "__main__":
    app.run()
