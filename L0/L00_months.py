# КАТАЛОГ ПРОЕКТА: МЕСЯЦЫ

import enum


MONTHS_S = ["", "янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]


class MONTHS(enum.Enum):
	""" Месяцы """

	JAN =  1
	FEB =  2
	MAR =  3
	APR =  4
	MAY =  5
	JUN =  6
	JUL =  7
	AUG =  8
	SEP =  9
	OCT = 10
	NOV = 11
	DEC = 12

	def __init__(self, code: int):
		self.code   = code
		self.name_s = MONTHS_S[code]

	def __str__(self) -> str:
		return self.name_s

	@classmethod
	def FindByNameS(cls, text: str) -> 'MONTHS':
		""" Поиск по имени """
		try   : return MONTHS(MONTHS_S.index(text))
		except: raise
