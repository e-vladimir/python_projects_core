# КАТАЛОГ: КОДЫ СОСТОЯНИЯ
# 11 июн 2024

import enum


class CODES(enum.Enum):
	""" Мета-структура группы кодов состояния """
	def __init__(self, code: int, description: str):
		self.code        = code
		self.description = description


# 00 - Завершение
class CODES_COMPLETION(CODES):
	COMPLETED   = (0, "Завершено")
	INTERRUPTED = (1, "Прервано")


# 01 - Выполнение
class CODES_PROCESSING(CODES):
	SKIP    = (1000, "Пропуск выполнения")
	PARTIAL = (1001, "Частичное выполнение")


# 02 - Данные
class CODES_DATA(CODES):
	NO_DATA       = (2000, "Данные отсутствуют")
	SINGLE        = (2001, "Данные в единичном экземпляре")
	NOT_ENOUGH    = (2002, "Данных недостаточно")
	ERROR_CONVERT = (2003, "Ошибка преобразования данных")
	ERROR_CHECK   = (2004, "Ошибка проверки или валидации")
	ERROR_TYPE    = (2005, "Ошибка типа данных")


# 03 - СУБД/SQL
class CODES_DB(CODES):
	NO_CONNECTION    = (3000, "Подключение отсутствует")
	ERROR_CONNECTION = (3001, "Ошибка подключения")
	ERROR_DB         = (3002, "Ошибка БД")
	ERROR_SQL        = (3003, "Ошибка SQL")
