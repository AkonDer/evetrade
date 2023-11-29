import json


def load_config():
    with open('config.json', 'r', encoding='utf-8') as file:
        return json.load(file)


# Загрузка конфигурации при импорте модуля
CONFIG = load_config()
