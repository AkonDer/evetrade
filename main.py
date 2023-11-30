import os
import time
import threading
from config import CONFIG
from database import load_data_to_db, session, clear_database
from helper import extract_module_name


def scan_directory(directory, known_files):
    try:
        current_files = set(os.listdir(directory))
        new_files = current_files - known_files
        if new_files:
            print("Обнаружены новые файлы:")
            for file in new_files:
                print(file)
                # Загрузка данных из файла в базу данных
                file_path = os.path.join(directory, file)
                load_data_to_db(file_path, extract_module_name(file))
                os.remove(file_path)
        return current_files
    except FileNotFoundError:
        print(f"Директория {directory} не найдена.")
        return known_files
    except PermissionError:
        print(f"Нет разрешения на доступ к директории {directory}.")
        return known_files


def directory_monitor(directory):
    known_files = set()
    while True:
        known_files = scan_directory(directory, known_files)
        time.sleep(CONFIG['SCAN_INTERVAL'])  # Пауза между проверками на основе конфигурации


def start_monitoring_thread(directory_path):
    monitor_thread = threading.Thread(target=directory_monitor, args=(directory_path,), daemon=True)
    monitor_thread.start()
    return monitor_thread


# Путь к директории
directory_path = CONFIG['PATH_TO_LOG']

# Интервал сканирования
CONFIG['SCAN_INTERVAL'] = 1

# Запуск мониторинга в отдельном потоке
monitor_thread = start_monitoring_thread(directory_path)

# Основной поток программы может продолжать выполнять другие задачи
try:
    while True:
        user_input = input("Введите 'd' для очистки базы данных, 'exit' для выхода: ").strip().lower()
        if user_input == 'd':
            print("Очищаем базу данных...")
            clear_database(session)
            print("База данных очищена.")
        elif user_input == 'exit':
            print("Программа остановлена пользователем.")
            break
        else:
            print("Неизвестная команда.")
except KeyboardInterrupt:
    print("Программа остановлена пользователем.")