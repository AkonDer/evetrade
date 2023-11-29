from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from models import MarketLog, Base
from helper import extract_module_name
from config import CONFIG

# Установка параметров подключения к базе данных SQLite
engine = create_engine('sqlite:///market_logs.db')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()


def load_data_to_db(filename, module_name):
    # Считывание данных из файла
    with open(filename, 'r') as file:
        lines = file.readlines()[1:]  # Пропускаем заголовок

        # Проверка и удаление существующих записей с тем же названием
        existing_records = session.query(MarketLog).filter(MarketLog.name == module_name).all()
        if existing_records:
            print(f"Удаляем существующие записи с названием {module_name}")
            for record in existing_records:
                session.delete(record)
            session.commit()

        for line in lines:
            data = line.strip().split(',')
            # Создание нового объекта MarketLog для каждой строки данных
            market_log = MarketLog(
                name=module_name,
                recordDate=datetime.now(),  # Изменено на текущую дату и время
                price=float(data[0]),
                volRemaining=int(float(data[1])),  # Конвертация в int, если число не целое
                typeID=int(data[2]),
                range=data[3],
                orderID=int(data[4]),
                volEntered=int(data[5]),
                minVolume=int(data[6]),
                bid=data[7] == 'True',
                issueDate=datetime.strptime(data[8], '%Y-%m-%d %H:%M:%S.%f'),
                duration=int(data[9]),
                stationID=int(data[10]),
                regionID=int(data[11]),
                solarSystemID=int(data[12]),
                jumps=int(data[13])
            )
            session.add(market_log)
    # Фиксация (сохранение) изменений в базе данных
    session.commit()


# Функция для очистки базы данных
def clear_database(session):
    # Удаление всех записей из всех таблиц
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()


