import requests


# Currency Conversion
def convert_currency(self, amount, from_currency, to_currency):
    try:
        # API endpoint for getting the latest rates for the from_currency
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url)
        response.raise_for_status()

        # Get the conversion rate for the desired currency
        rates = response.json().get('rates', {})
        conversion_rate = rates.get(to_currency, 1)

        # Calculate the converted amount
        converted_amount = round(amount * conversion_rate, 2)
        return converted_amount
    except requests.exceptions.RequestException as e:
        self.show_notification(f"Currency conversion failed: {str(e)}", "error")
        return amount
