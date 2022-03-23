import requests

api_key = 'bc03bdcb76770501b00df818f2f3607b'

# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


city = input("Stadt: ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

data = requests.get(url).json()

temperatur = data['main']['temp']
feuchtigkeit = data['main']['humidity']

print(data)
print("1. Temperatur: ", temperatur, "   2. Feuchtigkeit: ", feuchtigkeit)
