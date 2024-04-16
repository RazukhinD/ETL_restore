import requests
import json

api_key = 'dbrKFnXTyvxi38gkAzul8UxeZpGybdlt'

# Список городов для запроса данных о погоде
cities = ['Moscow', 'New York', 'Tokyo']

# Словарь для хранения данных о погоде в каждом городе
weather_data = {}

# Запрос данных о погоде для каждого города
for city in cities:
    url = f'https://api.tomorrow.io/v4/timelines?location={city}&fields=temperature&timesteps=current&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    weather_data[city] = data

# Вывод полученных данных
for city, data in weather_data.items():
    print(f"Weather in {city}:")
    print(data)
    print()

# Сохранение полученных данных в файл JSON
with open('weather_data_tomorrowio.json', 'w') as file:
    json.dump(weather_data, file)

print("Данные о погоде сохранены в файл 'weather_data_tomorrowio.json'")
