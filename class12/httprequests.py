import requests

# Get the response from the API endpoint
response = requests.get(
    "https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json")

# Get the status code from the response
print(response.status_code)

# Get the text from the response
print(response.text)

# Get the JSON data from the response
print(response.json().get("quoteText"))
