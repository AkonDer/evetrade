import requests

# URL для EVE Swagger Interface
esi_url = "https://esi.evetech.net/latest/"

# Конечная точка API для получения информации о структурах во вселенной
endpoint = "dogma/attributes/"

# Полный URL для запроса
url = esi_url + endpoint

# Выполнение GET-запроса к EVE Swagger Interface
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    data = response.json()  # Данные успешно получены
else:
    data = f"Error: {response.status_code}"  # Ошибка при выполнении запроса

print(data)
