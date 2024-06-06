# ПАЛИТРА ИНСТРУМЕТОВ ДЛЯ РАБОТЫ С ДАТОЙ-ВРЕМЕНЕМ
# 2024-06-06

import datetime
import time

from   G10_math_linear import Sign


DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# UNIX-ВРЕМЯ
def CurrentUTime() -> int:
	""" Получение текущего времени в UNIX-формате """
	return int(time.time())


# ТЕКУЩИЕ ДАННЫЕ
def CurrentDTime() -> datetime.datetime:
	""" Текущая дата-время """
	return datetime.datetime.now()


def CurrentDy() -> int:
	""" Текущий год 0..9999 """
	return CurrentDTime().year


def CurrentDm(flag_start_from_0: bool = False) -> int:
	""" Текущий месяц в виде 1..12|0..11 """
	current_month : int = CurrentDTime().month

	if flag_start_from_0: return current_month - 1

	return current_month


def CurrentDd() -> int:
	""" Текущее число месяца 1..31 """
	return CurrentDTime().day


# СМЕЩЕНИЕ ДАТ
def CalcDyDmByShiftDm(year: int, month: int, shift: int) -> tuple[int, int]:
	""" Вычисление года и месяца при смещении по месяцу """
	_year  : int = year
	_month : int = month - 1
	_month      += shift

	if _month < 0: _month -= 12

	_year  += Sign(_month) * (abs(_month) // 12)
	_month  = _month  % 12
	_month += 1

	return _year, _month


# ПРЕОБРАЗОВАНИЕ
def DTimeToUTime(dtime: datetime.datetime) -> int:
	""" Преобразование datetime в unix-формат """
	return int(dtime.timestamp())


def UTimeToDTime(utime: int) -> datetime.datetime:
	""" Преобразование unix формата в datetime """
	return datetime.datetime.fromtimestamp(utime)


# ФОРМИРОВАНИЕ ДАННЫХ
def DyDmDdToUTime(year: int, month: int = None, day: int = None, flag_end_day: bool = False) -> int:
	""" Преобразование ГГГГ.ММ.ДД в unix-формат. Примечание: месяц 1..12, число 1..31 """
	dy     : int = year
	dm     : int = 1
	dd     : int = 1

	if month is not None:
		if month in range(1, 13): dm = month

	if day is not None:
		if day in range(1, 32)  : dd = day

	max_dd : int = DAYS_IN_MONTH[dm - 1]
	max_dd      += 1 if (dy % 4 == 0) else 0

	dd           = min(dd, max_dd)

	hh     : int = 0
	hm     : int = 0
	hs     : int = 0
	hs6    : int = 0

	if flag_end_day:
		hh = 23
		hm = 59
		hs = 59

	dtime = datetime.datetime(year=dy, month=dm, day=dd, hour=hh, minute=hm, second=hs, microsecond=hs6)

	return DTimeToUTime(dtime)


# ===[ НА РАЗБОР ]===
# def DTime(dy, dm, dd, hh, hm, hs, utc_shift: Union[int , str] = None):
# 	""" Создание datetime с указанным часовым поясом """
# 	if        utc_shift  is None: return datetime.datetime(year=dy, month=dm, day=dd, hour=hh, minute=hm, second=hs)
# 	elif type(utc_shift) is int : return datetime.datetime(year=dy, month=dm, day=dd, hour=hh, minute=hm, second=hs, tzinfo=datetime.timezone(datetime.timedelta(minutes=utc_shift)))
# 	elif type(utc_shift) is str :
# 		try   : return datetime.datetime(year=dy, month=dm, day=dd, hour=hh, minute=hm, second=hs, tzinfo=pytz.timezone(utc_shift))
# 		except: return datetime.datetime(year=dy, month=dm, day=dd, hour=hh, minute=hm, second=hs)
#
#
# def CurrentDTime(utc_shift: Union[int, str] = None):
# 	""" Текущее значение DTime """
# 	if        utc_shift  is None: return datetime.datetime.now()
# 	elif type(utc_shift) is int : return datetime.datetime.now(datetime.timezone(datetime.timedelta(minutes=utc_shift)))
# 	elif type(utc_shift) is str :
# 		try   : return datetime.datetime.now(pytz.timezone(utc_shift))
# 		except: return datetime.datetime.now()
#
#
# def CurrentDTimeUtc():
# 	""" Текущее значение DTime """
# 	return datetime.datetime.now(datetime.timezone.utc)
#
#
# def CurrentUTime():
# 	""" Текущее значение UTime """
# 	return int(CurrentDTime().timestamp())
#
#
# def CurrentDayOfWeek(utc_shift: Union[int, str] = 0):
# 	""" Текущий день недели [1..7] """
# 	return CurrentDTime(utc_shift).weekday() + 1
#
#
# def CurrentDy(utc_shift : Union[int, str] = None):
# 	""" Текущий час """
# 	return CurrentDTime(utc_shift).year
#
#
# def CurrentDm(utc_shift : Union[int, str] = None):
# 	""" Текущая минута """
# 	return CurrentDTime(utc_shift).month
#
#
# def CurrentDd(utc_shift : Union[int, str] = None):
# 	""" Текущая секунда """
# 	return CurrentDTime(utc_shift).day
#
#
# def CurrentHh(utc_shift : Union[int, str] = None):
# 	""" Текущий час """
# 	return CurrentDTime(utc_shift).hour
#
#
# def CurrentHm(utc_shift : Union[int, str] = None):
# 	""" Текущая минута """
# 	return CurrentDTime(utc_shift).minute
#
#
# def CurrentHs(utc_shift : Union[int, str] = None):
# 	""" Текущая секунда """
# 	return CurrentDTime(utc_shift).second
#
#
# def UTimeToDTime(in_utime: int, utc_shift : Union[int, str] = None):
# 	""" Конвертация UTime в DTime """
# 	if        utc_shift  is None: return datetime.datetime.fromtimestamp(in_utime)
# 	elif type(utc_shift) is int : return datetime.datetime.fromtimestamp(in_utime, datetime.timezone(datetime.timedelta(minutes=utc_shift)))
# 	elif type(utc_shift) is str :
# 		try   : return datetime.datetime.fromtimestamp(in_utime, pytz.timezone(utc_shift))
# 		except: return datetime.datetime.fromtimestamp(in_utime)
#
#
# def DTimeToUTime(in_dtime: datetime.datetime):
# 	""" Конвертация DTime в UTime """
# 	return int(in_dtime.timestamp())
#
#
# def DeltaDdForUTime(in_utime_0: int, in_utime_1: int):
# 	""" Вычисление разницы в днях между UTime """
# 	dtime_0 = UTimeToDTime(in_utime_0)
# 	dtime_1 = UTimeToDTime(in_utime_1)
#
# 	delta   = dtime_1 - dtime_0
#
# 	return delta.days + 1
#
#
# def DeltaHhForUTime(in_utime_0: int, in_utime_1: int):
# 	""" Вычисление разницы в часах между UTime """
# 	dtime_0 = UTimeToDTime(in_utime_0)
# 	dtime_1 = UTimeToDTime(in_utime_1)
#
# 	delta   = dtime_1 - dtime_0
#
# 	return delta.total_seconds() // 3600
#
#
# def ShiftUTime(utime: int, shift: int = 0) -> int:
# 	""" Смещение UTime на указанное количество часов """
# 	if shift == 0: return utime
#
# 	_dtime_delta = datetime.timedelta(hours=abs(shift))
# 	_dtime = UTimeToDTime(utime)
#
# 	if shift > 0: _dtime += _dtime_delta
# 	else:         _dtime -= _dtime_delta
#
# 	return DTimeToUTime(_dtime)
#
#
# # РАБОТА С ПЕРИОДАМИ 0..-24
# def Month_0():
# 	""" Возвращает dtime_0, dtime_1 для месяца 0 """
# 	dtime_now = CurrentDTime()
# 	dtime_0   = dtime_now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
#
# 	delta_1s  = datetime.timedelta(seconds=1)
#
# 	dtime_1   = dtime_0 - delta_1s
# 	dtime_0   = dtime_1.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
#
# 	return dtime_0, dtime_1
#
#
# def MonthPrev(in_count_prev: int):
# 	""" Возвращает dtime_0, dtime_1 для месяца -<указатель> """
# 	delta_1s         = datetime.timedelta(seconds=1)
# 	dtime_0, dtime_1 = Month_0()
#
# 	for index in range(in_count_prev):
# 		dtime_1 = dtime_0 - delta_1s
# 		dtime_0 = dtime_1.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
#
# 	return dtime_0, dtime_1
