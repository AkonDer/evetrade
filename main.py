import os
import time
import threading
from config import CONFIG


def scan_directory(directory, known_files):
    try:
        current_files = set(os.listdir(directory))
        new_files = current_files - known_files
        if new_files:
            print("Обнаружены новые файлы:")
            for file in new_files:
                print(file)
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
        time.sleep(1)  # Пауза в 5 секунд между проверками


def start_monitoring_thread(directory_path):
    monitor_thread = threading.Thread(target=directory_monitor, args=(directory_path,), daemon=True)
    monitor_thread.start()
    return monitor_thread


# Путь к директории
directory_path = CONFIG['PATH_TO_LOG']

# Запуск мониторинга в отдельном потоке
monitor_thread = start_monitoring_thread(directory_path)

# Основной поток программы может продолжать выполнять другие задачи
try:
    while True:
        time.sleep(1)  # Для примера, основной поток просто ждёт
except KeyboardInterrupt:
    print("Программа остановлена пользователем.")
