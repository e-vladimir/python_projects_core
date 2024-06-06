# КОНВЕРТОР: ДАННЫЕ
# 2024-06-06

def AmountToString(amount: float | int, flag_point: bool = False, flag_sign: bool = False) -> str:
	""" Конвертация суммы в строку с разделением триад """
	if flag_point: return f"{'+' if (flag_sign and amount > 0) else ''}{amount:,.2f}".replace(',', ' ')
	else:          return f"{'+' if (flag_sign and amount > 0) else ''}{amount:,.0f}".replace(',', ' ')


def SecondsToThTmTs(seconds: int) -> str:
	""" Конвертация количества секунд в ЧЧ:ММ:СС """
	th : int = seconds // 3600
	tm : int = (seconds % 3600) // 60
	ts : int = seconds % 60

	return f"{th:02d}ч {tm:02d}м {ts:02d}с"
