import requests
import json
from requests.exceptions import HTTPError
from flask import Flask, request

#Creating the Flask application
app = Flask('app')


#This function retrieves the average exchange rate for a speciic arguments(table, currency code, date) from the NBP API and reutrns data as a JSON object
@app.route('/avg', methods=['GET'])
def get_avg_exchange_rate():

  try:
    table = request.args.get('table') #Get table parametr from given URL
    code = request.args.get('code') #Get code parametr from given URL
    date = request.args.get('date') #Get topCount(days) parametr from given URL
    url = f'http://api.nbp.pl/api/' \
          f'exchangerates/rates/{table}/' \
          f'{code}/' \
          f'{date}/' \
          f'?format=json'
    response = requests.get(url)  #Sending request to API
    response.raise_for_status()  #Raising an error if status code != 200

  #Handling each error that may occur
  except HTTPError as http_error:
    print(f'HTTP Error: {http_error}')
    return "Error" + str(response.status_code)

  except requests.exceptions.TooManyRedirects as redirects_error:
    print(f'Too many redirets Error: {redirects_error}')
    return "Error: Too many redirects Error"

  except requests.exceptions.Timeout as timeout_error:
    print(f'Requests Timeout Error: {timeout_error} ')
    return "Error: Request Timeout Error"

  except requests.exceptions.RequestException as other_error:
    print(f'Other exception: {other_error}')
    return "Error" + str(response.status_code)

  else:
    if response.status_code == 200:
      data = response.json() #Convert response Json to a dictionary
      avg = data['rates'][0]['mid'] #Retrive the average exchange rate
      return json.dumps(avg, indent=4) #Returns data as a JSON string

    else:
      return "Error... " + str(response.status_code)


#This function retrieves the maximum difference between bis and ask prices for a specific arguments(table, currency code, topCount) from the NBP API for specified days parameter and returns string
@app.route('/max-min-rate', methods=['GET'])
def get_max_min_rate():
  try:
    table = request.args.get('table') #Get table parametr from given URL
    code = request.args.get('code') #Get code parametr from given URL
    num_of_topCount = request.args.get('topCount') #Get topCount(days) parametr from given URL
    if num_of_topCount > 255:
      return "Error: topCOunt must be less than or equal 255"

    #Building API URL
    url = f'http://api.nbp.pl/api/' \
          f'exchangerates/rates/{table}/' \
          f'{code}/last/' \
          f'{num_of_topCount}/' \
          f'?format=json'
    response = requests.get(url)  #Sending request to API
    response.raise_for_status()  #Raising an error if status code != 200

  #Handling each error that may occur
  except HTTPError as http_error:
    print(f'HTTP Error: {http_error}')
    return "Error" + str(response.status_code)

  except requests.exceptions.TooManyRedirects as redirects_error:
    print(f'Too many redirets Error: {redirects_error}')
    return "Error: Too many redirects Error"

  except requests.exceptions.Timeout as timeout_error:
    print(f'Requests Timeout Error: {timeout_error} ')
    return "Error: Request Timeout Error"

  except requests.exceptions.RequestException as other_error:
    print(f'Other exception: {other_error}')
    return "Error" + str(response.status_code)

  else:
    if response.status_code == 200:
      data = response.json() #Convert response Json to a dictionary
      rates = [r['mid'] for r in data['rates']] #Creating list that contains all the mid values from rates 
      max_rate = max(rates) #Getting max value from rates and stores them in max_rate
      min_rate = min(rates) #Getting min value from rates and stores them in min_rate
      return f"Max: {max_rate}, Min: {min_rate}" #Returns data as a String
    else:
      return "Error... " + str(response.status_code)


#This function retrieves the maximum difference between bid ans adk prices for a specific arguments(table, currency code, topCount) from the NBP API for specified days parameter and returns string
@app.route('/buy-ask', methods=['GET'])
def get_buy_ask():
  try:
    table = request.args.get('table')  #Get table parametr from given URL
    code = request.args.get('code')  #Get code parametr from given URL
    num_of_topCount = request.args.get(
      'topCount')  #Get topCount(days) parametr from given URL
    if num_of_topCount > 255:
      return "Error: topCOunt must be less than or equal 255"

    #Building API URL
    url = f'http://api.nbp.pl/api/' \
          f'exchangerates/rates/{table}/' \
          f'{code}/last/' \
          f'{num_of_topCount}/' \
          f'?format=json'
    response = requests.get(url)  #Sending request to API
    response.raise_for_status()  # Raising an error if status code != 200

  #Handling each error that may occur
  except HTTPError as http_error:
    print(f'HTTP Error: {http_error}')
    return "Error" + str(response.status_code)

  except requests.exceptions.TooManyRedirects as redirects_error:
    print(f'Too many redirets Error: {redirects_error}')
    return "Error: Too many redirects Error"

  except requests.exceptions.Timeout as timeout_error:
    print(f'Requests Timeout Error: {timeout_error} ')
    return "Error: Request Timeout Error"

  except requests.exceptions.RequestException as other_error:
    print(f'Other exception: {other_error}')
    return "Error" + str(response.status_code)

  else:
    if response.status_code == 200:
      data = response.json()  #Convert response Json to a dictionary
      differents_list = [
        abs(r['bid'] - r['ask']) for r in data['rates']
      ]  #Creating list of differences between bid and ask prices for each currency rate
      max_differents = max(
        differents_list)  #Finging max difference in the list
      return str(max_differents)

    else:
      return "Error... " + str(response.status_code)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
