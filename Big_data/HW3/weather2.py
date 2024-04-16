import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from hdfs import InsecureClient

# Загрузка данных из файла JSON
with open('weather_data_tomorrowio.json', 'r') as file:
    weather_data = json.load(file)

# Создание DataFrame для хранения данных о температуре
temperature_data = []

for city, data in weather_data.items():
    temperature = data['data']['timelines'][0]['intervals'][0]['values']['temperature']
    temperature_data.append((city, temperature))

df = pd.DataFrame(temperature_data, columns=['City', 'Temperature'])

# Построение графиков изменения температуры в разных городах
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='City', y='Temperature', marker='o')
plt.title('Temperature Change in Different Cities')
plt.xlabel('Cities')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig('temperature_change.png')
plt.show()

# Построение графика распределения температуры
plt.figure(figsize=(8, 6))
sns.histplot(df['Temperature'], bins=10, kde=True)
plt.title('Temperature Distribution')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.savefig('temperature_distribution.png')
plt.show()

# Сохранение результатов в HDFS
client = InsecureClient('http://localhost:50070')
with client.write('/user/weather/temperature_change.png', encoding='utf-8') as writer:
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='City', y='Temperature', marker='o')
    plt.title('Temperature Change in Different Cities')
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(writer)

with client.write('/user/weather/temperature_distribution.png', encoding='utf-8') as writer:
    plt.figure(figsize=(8, 6))
    sns.histplot(df['Temperature'], bins=10, kde=True)
    plt.title('Temperature Distribution')
    plt.xlabel('Temperature (°C)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(writer)

# Выгрузка результатов из HDFS на локальный компьютер
client.download('/user/weather/temperature_change.png', 'temperature_change_hdfs.png', overwrite=True)
client.download('/user/weather/temperature_distribution.png', 'temperature_distribution_hdfs.png', overwrite=True)

print("Графики успешно сохранены в HDFS и загружены на локальный компьютер.")
