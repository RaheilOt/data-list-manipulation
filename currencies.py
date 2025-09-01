# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {
    "USDEUR": 0.85,   # 1 USD = 0.85 EUR
    "GBPEUR": 1.13,   # 1 GBP = 1.13 EUR
    "CHFEUR": 0.86,   # 1 CHF = 0.86 EUR
    "EURGBP": 0.885   # 1 EUR = 0.885 GBP
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    value, from_currency = amount
    key = from_currency + currency  # construct key like "USDEUR"

    # If the rate does not exist, return None
    if key not in RATES:
        return None

    # Convert and round the result
    return round(value * RATES[key])