#Q-1 Get the Following Data from the url using opps & json
# 1) Method to fetch the data 
# 2) Method to get data of name currency symbol
# 3) Method to get data of Dollar Countries
# 4) Method to get the data of Euro Countries



import requests
import json

class Country_Info:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        store_data = requests.get(self.url)
        return store_data.json()

    def fetch_name_currency_symbol(self):
        data_n_c_s = []
        for data in self.fetch_data():
            name_info = data.get('name')
            common_name = name_info.get('common')
            currencies = data.get('currencies')
            symbols = []  # Initialize symbols as an empty list for each country

            if currencies:
                for currency in currencies:
                    symbol_name = currencies[currency].get('symbol', '')
                    symbols.append(symbol_name)

            data_n_c_s.append({'name': common_name, 'currencies': currencies, 'symbols': symbols})

        return data_n_c_s
    
    def countries_with_dollar(self):
        data = self.fetch_data()
        dollar_countries = []

        for entry in data:
            name_info = entry.get('name')
            common_name = name_info.get('common')
            currencies = entry.get('currencies')
            
            if currencies:
                for currency in currencies:
                    currency_name = currencies[currency].get('name', '').lower()
                    
                    if 'dollar' in currency_name:
                        dollar_countries.append(common_name)

        return dollar_countries

    def countries_with_euro(self):
        data = self.fetch_data()
        euro_countries = []

        for entry in data:
            name_info = entry.get('name')
            common_name = name_info.get('common')
            currencies = entry.get('currencies')
            
            if currencies:
                for currency in currencies:
                    currency_name = currencies[currency].get('name', '').lower()
                    
                    if 'euro' in currency_name:
                        euro_countries.append(common_name)

        return euro_countries

url = "https://restcountries.com/v3.1/all"
country_data = Country_Info(url)

name_currency_symbol_data = country_data.fetch_name_currency_symbol()
for entry in name_currency_symbol_data:
    print("Country Name:", entry['name'])
    print("Currencies:", entry['currencies'])
    print("Symbols:", entry['symbols'])

dollar_countries = country_data.countries_with_dollar()
print("Countries with 'Dollar' in their currencies:")
for country in dollar_countries:
    print(country)

euro_countries = country_data.countries_with_euro()
print("Countries with 'Euro' in their currencies:")
for country in euro_countries:
    print(country)














#  Q2 Get the following data
# Breweries from New York,Alaska,Maine
# count the breweries in the given states
# count the type of breweries in the given state
# count the breweries with websites and list it


import requests

class BreweryDB:
    BASE_URL = "https://api.openbrewerydb.org/breweries"

    def __init__(self):
        self.breweries = []

    def get_breweries_by_state(self, state):
        params = {"by_state": state}
        response = requests.get(self.BASE_URL, params=params)
        self.breweries = response.json()
       

    def count_breweries_in_state(self, state):
        self.get_breweries_by_state(state)
        return len(self.breweries)

    def count_unique_brewery_types_in_state(self, state):
        self.get_breweries_by_state(state)
        unique_types = set(brewery['brewery_type'] for brewery in self.breweries)
        return len(unique_types)

    def count_breweries_with_websites_in_state(self, state):
        self.get_breweries_by_state(state)
        breweries_with_websites = [brewery for brewery in self.breweries if brewery.get('website_url')]
        return len(breweries_with_websites)

    def list_breweries_with_websites_in_state(self, state):
        self.get_breweries_by_state(state)
        breweries_with_websites = [brewery for brewery in self.breweries if brewery.get('website_url')]
        return breweries_with_websites

states = ["Alaska", "New York", "Maine"]

for state in states:
    brewery_db = BreweryDB()
    
    brewery_count = brewery_db.count_breweries_in_state(state)
    unique_type_count = brewery_db.count_unique_brewery_types_in_state(state)
    websites_count = brewery_db.count_breweries_with_websites_in_state(state)
    breweries_with_websites = brewery_db.list_breweries_with_websites_in_state(state)

    print(f"Breweries in {state}:")
    for brewery in brewery_db.breweries:
        print(f"- {brewery['name']} in {brewery['city']} (Type: {brewery['brewery_type']})")

    print(f"Total number of breweries in {state}: {brewery_count}")
    print(f"Number of unique brewery types in {state}: {unique_type_count}")
    print(f"Number of breweries with websites in {state}: {websites_count}")

    if websites_count > 0:
        print(f"Breweries with websites in {state}:")
        for brewery in breweries_with_websites:
            print(f"- {brewery['name']} ({brewery['website_url']})")

    print()
















    