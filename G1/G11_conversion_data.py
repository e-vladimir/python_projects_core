# КОНВЕРТАЦИЯ: ДАННЫЕ
# 18 авг 2025

import datetime

from   G10_conversion_format import UTimeToDTime


SEPARATOR_LIST    = ' '
SEPARATOR_SUBLIST = '|'

DAYS              = [["Понедельник", "Пн"],
					 ["Вторник",     "Вт"],
					 ["Среда",       "Ср"],
					 ["Четверг",     "Чт"],
					 ["Пятница",     "Пт"],
					 ["Суббота",     "Сб"],
					 ["Воскресенье", "Вс"]]


MONTHS            = ["", "янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]


DATA_TRANSLITERATION : dict[str, str] = dict()
DATA_TRANSLITERATION['а'] = "a"
DATA_TRANSLITERATION['б'] = "b"
DATA_TRANSLITERATION['в'] = "v"
DATA_TRANSLITERATION['г'] = "g"
DATA_TRANSLITERATION['д'] = "d"
DATA_TRANSLITERATION['е'] = "e"
DATA_TRANSLITERATION['ё'] = "e"
DATA_TRANSLITERATION['ж'] = "zh"
DATA_TRANSLITERATION['з'] = "z"

DATA_TRANSLITERATION['и'] = "i"
DATA_TRANSLITERATION['й'] = "y"
DATA_TRANSLITERATION['к'] = "k"
DATA_TRANSLITERATION['л'] = "l"
DATA_TRANSLITERATION['м'] = "m"
DATA_TRANSLITERATION['н'] = "n"
DATA_TRANSLITERATION['о'] = "o"
DATA_TRANSLITERATION['п'] = "p"
DATA_TRANSLITERATION['р'] = "r"

DATA_TRANSLITERATION['с'] = "s"
DATA_TRANSLITERATION['т'] = "t"
DATA_TRANSLITERATION['у'] = "u"
DATA_TRANSLITERATION['ф'] = "f"
DATA_TRANSLITERATION['х'] = "kh"
DATA_TRANSLITERATION['ц'] = "ts"
DATA_TRANSLITERATION['ч'] = "ch"
DATA_TRANSLITERATION['ш'] = "sh"
DATA_TRANSLITERATION['щ'] = "shch"

DATA_TRANSLITERATION['ъ'] = ""
DATA_TRANSLITERATION['ы'] = "y"
DATA_TRANSLITERATION['ь'] = ""
DATA_TRANSLITERATION['э'] = "e"
DATA_TRANSLITERATION['ю'] = "yu"
DATA_TRANSLITERATION['я'] = "ya"

DATA_TRANSLITERATION[' '] = "_"


# ЧИСЛА И СУММЫ
def AmountToString(amount: float | int | None, flag_point: bool = False, flag_sign: bool = False) -> str:
	""" Конвертация суммы в строку с разделением триад """
	if amount is None: return ""

	if flag_point    : return f"{'+' if (flag_sign and amount > 0) else ''}{amount:,.2f}".replace(',', ' ')
	else             : return f"{'+' if (flag_sign and amount > 0) else ''}{amount:,.0f}".replace(',', ' ')


# ДАТА И ВРЕМЯ
def UTimeToDdDmDyThTmTs(in_utime: int, utc_shift: int | str = None, flag_include_thtmts: bool = True) -> str:
	""" Конвертация UTime в строковый вид  """
	dtime  : datetime.datetime = UTimeToDTime(in_utime, utc_shift)

	if in_utime <= 0         : return "Нет данных"
	elif flag_include_thtmts : return f"{dtime:%d %h %Y %H:%M}"
	else                     : return f"{dtime:%d %h %Y}"


def UTimeToThTmTs(utime: int, utc_shift: str = "") -> str:
	""" Преобразование Unix-времени в ЧЧ:ММ """
	dtime    = UTimeToDTime(utime, utc_shift)

	th : str = f"{dtime.hour:02d}"
	tm : str = f"{dtime.minute:02d}"
	ts : str = f"{dtime.second:02d}"

	return f"{th}:{tm}:{ts}"


def DTimeToDyDmDd(dtime: datetime.datetime, dm_as_string: bool = False) -> str:
	""" Преобразование даты/времени в красивую строку """
	dd : str = f"{dtime.day:02d}"
	dm : str = MONTHS[dtime.month] if dm_as_string else f"{dtime.month:02d}"
	dy : str = f"{dtime.year:04d}"

	return f"{dd} {dm} {dy}"


def UTimeToDyDmDd(utime: int, utc_shift: str = "", dm_as_string: bool = False) -> str:
	""" Преобразование Unix-времени в красивую строку """
	dtime    = UTimeToDTime(utime, utc_shift)

	dd : str = f"{dtime.day:02d}"
	dm : str = MONTHS[dtime.month] if dm_as_string else f"{dtime.month:02d}"
	dy : str = f"{dtime.year:04d}"

	return f"{dd} {dm} {dy}"


def DwToString(in_index: int, short_format: bool = False) -> str:
	""" Преобразование индекса дня недели [1..7] в название """
	try   : return DAYS[in_index - 1][int(short_format)]
	except: return ""


def SecondsToThTmTs(seconds: int, flag_include_labels: bool = True) -> str:
	""" Конвертация количества секунд в ЧЧ:ММ:СС """
	th : int =  seconds // 3600
	tm : int = (seconds %  3600) // 60
	ts : int =  seconds %    60

	if flag_include_labels: return f"{th:02d}ч {tm:02d}м {ts:02d}с"
	else                  : return f"{th:02d}:{tm:02d}:{ts:02d}"


# КООРДИНАТЫ
def PointToString(in_point_or_x, in_y: int = None) -> str:
	""" Преобразование координат в строку из массива или по отдельным координатам """
	if   type(in_point_or_x) is list :
		try   : return f"{in_point_or_x[0]} {in_point_or_x[1]}"
		except:	return ""
		
	elif type(in_point_or_x) is tuple:
		try   : return f"{in_point_or_x[0]} {in_point_or_x[1]}"
		except:	return ""
		
	elif in_y                is None :
		return ""
	
	else                             :
		return f"{in_point_or_x} {in_y}"


def StringToPoint(in_str: str) -> tuple:
	""" Преобразование строки в массив координат """
	data = in_str.replace(',', ' ').split(' ')

	try   : return int(data[0]), int(data[1])
	except: return None, None


# НАБОРЫ
def ListToString(in_list: list) -> str:
	""" Преобразование списка 1-го уровня в строку """
	return SEPARATOR_LIST.join([f"{item}" for item in in_list])


def StringToList(in_str: str) -> list[str]:
	""" Преобразование строки в список 1-го уровня """
	return in_str.split(SEPARATOR_LIST)


def SublistToString(in_list: list) -> str:
	""" Преобразование списка 1-го уровня в строку """
	return SEPARATOR_SUBLIST.join([f"{item}" for item in in_list])


def StringToSublist(in_str: str) -> list[str]:
	""" Преобразование строки в список 1-го уровня """
	return in_str.split(SEPARATOR_SUBLIST)


# ТЕКСТ
def Transliterate(text_src: str) -> str:
	""" Транслитерация строки """
	result : str = ""

	for point in text_src.lower(): result += DATA_TRANSLITERATION.get(point, "_")

	return result
