import requests

def convert_currency(amount, from_currency, to_currency):
    try:
        url = (
            f"https://api.frankfurter.app/latest"
            f"?amount={amount}"
            f"&from={from_currency}"
            f"&to={to_currency}"
        )

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        converted_amount = data["rates"][to_currency]

        return converted_amount

    except Exception as e:
        return f"Error: {e}"