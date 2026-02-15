import requests

url = "https://api.frankfurter.app"

date = input("Please enter the date (in the format 'yyyy-mm-dd')")
base = input("Convert frome (Currency): ")
Currency = input("Convert to (Currency): ")
amount = float(input("How much {} would you like to convert?: ".format(base)))

url2 = url + "/" + date + "?base=" + base + "&symbols=" + Currency
response = requests.get(url2)

if(response.ok is False):
    print("\nError {}:".format(response.status_code))
else:
    data = response.json()
    rate = data['rates'][Currency]
    result = amount * rate
    print("\n{0} {1} was equal to {2} {3}, based on the exchange rate on {4}".format(amount, base, result, Currency, data['date']))
