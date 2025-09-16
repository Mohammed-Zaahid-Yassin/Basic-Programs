def currency_converter(amount, from_currency, to_currency, rates):
    if from_currency == to_currency:
        return amount
    try:
        base_amount = amount / rates[from_currency]
        converted = base_amount * rates[to_currency]
        return converted
    except KeyError:
        return None

rates = {
    "INR": 1,           # Base currency
    "USD": 0.013,
    "EUR": 0.012,
    "GBP": 0.010,
    "JPY": 1.45
}

print("Supported currencies:", ", ".join(rates.keys()))
amount = float(input("Enter amount to convert: "))
from_curr = input("From currency (e.g., INR): ").upper()
to_curr = input("To currency (e.g., USD): ").upper()

result = currency_converter(amount, from_curr, to_curr, rates)
if result is None:
    print("Unsupported currency code.")
else:
    print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
