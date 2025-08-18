# ЖУРНАЛИРОВАНИЕ
# 18 авг 2025

from G10_datetime import CurrentDTime

TYPE_ERROR   = "[E]"
TYPE_WARNING = "[!]"
TYPE_INFO    = "   "
TYPE_OK      = "[+]"
TYPE_NO      = "[-]"


def LogMessage(in_type: str, in_message: str):
	""" Общий метод вывода лога"""
	print(f"{CurrentDTime():%d %b %Y %H:%M:%S} {in_type} {in_message}")


def LogError(in_message: str):
	""" Ошибка """
	LogMessage(TYPE_ERROR, in_message)


def LogWarning(in_message: str):
	""" Предупреждение """
	LogMessage(TYPE_WARNING, in_message)


def LogInfo(in_message: str):
	""" Информация """
	LogMessage(TYPE_INFO, in_message)


def LogOk(in_message: str):
	""" Подтверждение """
	LogMessage(TYPE_OK, in_message)


def LogNo(in_message: str):
	""" Отмена """
	LogMessage(TYPE_NO, in_message)


def LogByStatus(in_type: str, in_message: str):
	""" Переводит статус сообщения в консольный и выводит сообщение """
	log_fun = status_translate[in_type]
	log_fun(in_message)
