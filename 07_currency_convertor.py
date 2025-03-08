from requests import get


def api_key(file_path):
    with open(file_path, "r") as f:
        key = f.read().strip()
    return key


BASE_URL = "https://api.currencyfreaks.com/v2.0/rates"
API_KEY = api_key("07_api_key.txt")

def currency_convertor(currency_input):
    convertor_endpoint = f"{BASE_URL}/latest?apikey={API_KEY}&symbols={currency_input}"

    # Sending the GET request
    response = get(convertor_endpoint)

    if response.status_code == 200:
        # Convert the response to JSON format
        data = response.json()['rates']
        return float(data[currency_input])
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


dollar_input = int(input("Enter the Dollar value for conversion: "))
currency_input = input("Convert from USD to the Currency: ")

convertion_rate = currency_convertor(currency_input)
if convertion_rate:
    converted_value = float(convertion_rate * dollar_input)

print(converted_value)

