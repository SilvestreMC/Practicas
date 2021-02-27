import requests

page = requests.get ("https://api.openweathermap.org/data/2.5/weather?q=Monterrey&appid=fa606d3cd1699ac41b0fc155f8a0d16d") 
print("OpenweatherAPI, El clima en Monterrey")
print (page.content)