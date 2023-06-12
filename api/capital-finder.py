from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    response_string =""
    url_path = self.path
    url_component = parse.urlsplit(url_path)
    query_var = parse.parse_qsl(url_component.query)
    my_dict = dict(query_var)
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    if 'country' in my_dict:
      country = my_dict.get('country')
      url_API = f'https://restcountries.com/v3.1/name/{country}'
      result_of_request = requests.get(url_API)
      json_data = result_of_request.json()
      
      
      for data in json_data:
        capital = data['capital'][0]
        response_string = f"The capital of {country} is {capital}."

    elif 'capital' in my_dict:
      capital = my_dict.get('capital')
      url_API = f'https://restcountries.com/v3.1/capital/{capital}'
      result_of_request = requests.get(url_API)
      json_data = result_of_request.json()

      for data in json_data:
        country = data['name']['common']
        response_string = f"{capital} is the capital of {country}."
            
    



    self.wfile.write(str(response_string).encode())
    return