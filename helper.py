import re


# Функция извлечения названия модуля из названия файла
def extract_module_name(filename):
    # Регулярное выражение теперь ищет любой текст перед первым дефисом
    match = re.search(r'^(.+?)-(.+?)-\d{4}\.\d{2}\.\d{2} \d{6}', filename)
    if match:
        # Возвращаем вторую группу захвата, которая соответствует названию модуля
        return match.group(2).strip()
    else:
        # Если совпадение не найдено, возвращаем None
        return None

