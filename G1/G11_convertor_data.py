# КОНВЕРТОР: ДАННЫЕ
# 03 фев 2025

import datetime

from   G10_convertor_format import UTimeToDTime


def AmountToString(amount: float | int | None, flag_point: bool = False, flag_sign: bool = False) -> str:
	""" Конвертация суммы в строку с разделением триад """
	if amount is None: return ""

	if flag_point    : return f"{'+' if (flag_sign and amount > 0) else ''}{amount:,.2f}".replace(',', ' ')
	else             : return f"{'+' if (flag_sign and amount > 0) else ''}{amount:,.0f}".replace(',', ' ')


# Время
def SecondsToThTmTs(seconds: int, flag_include_labels: bool = True) -> str:
	""" Конвертация количества секунд в ЧЧ:ММ:СС """
	th : int =  seconds // 3600
	tm : int = (seconds %  3600) // 60
	ts : int =  seconds %    60

	if flag_include_labels: return f"{th:02d}ч {tm:02d}м {ts:02d}с"
	else                  : return f"{th:02d}:{tm:02d}:{ts:02d}"


# Дата
def UTimeToDdDmDyThTmTs(in_utime: int, utc_shift: int | str = None, flag_include_thtmts: bool = True) -> str:
	""" Конвертация UTime в строковый вид  """
	dtime  : datetime.datetime = UTimeToDTime(in_utime, utc_shift)

	if in_utime <= 0         : return "Нет данных"
	elif flag_include_thtmts : return f"{dtime:%d %h %Y %H:%M}"
	else                     : return f"{dtime:%d %h %Y}"
