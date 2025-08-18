# МЕТА-ОБЪЕКТЫ
# 18 авг 2025

import statistics

from   G10_math_linear import AvgOrNone, MaxOrNone, MinOrNone


class C20_Buffer:
	""" Мета-буфер """
	
	def __init__(self, in_limit: int = 10):
		self._items :list = []
		self._limit : int = max(2, in_limit)

	# МОДЕЛЬ ДАННЫХ
	@property
	def limit(self) -> int:
		return self._limit
	@limit.setter
	def limit(self, count: int):
		self._limit = max(2, count)

	@property
	def size(self) -> int:
		return len(self._items)

	@property
	def items(self) -> list:
		return self._items[:]

	# МЕХАНИКА ДАННЫХ
	def Append(self, in_value):
		""" Добавление значения в буфер """
		self._items.append(in_value)
		self._items = self._items[-self.limit:]

	def Clear(self):
		""" Очистка буфера """
		self._items.clear()

	# ЛОГИКА ДАННЫХ
	def ImportFromList(self, in_list: list):
		""" Импорт значений в буфер """
		self._items = in_list[:]

	def CutL(self, in_count: int = 0):
		""" Срез буфера слева """
		self._items = self._items[in_count:]

	def CutR(self, in_count: int = 0):
		""" Срез буфера справа """
		self._items = self._items[:in_count]

	def CountOfValue(self, in_value):
		""" Подсчет количества совпадений """
		return len([item for item in self._items if item == in_value])

	def AvgOrNone(self) -> float | None:
		""" Вычисление среднего арифметического """
		return AvgOrNone(self._items)

	def SumOrNone(self) -> float | int | None:
		""" Сумма """
		try   : return sum(self._items)
		except: return None

	def MedOrNone(self) -> float | None:
		""" Медиана """
		try   : return statistics.median(self._items)
		except: return None

	def ModOrNone(self) -> float | int | None:
		""" Мода """
		try   : return statistics.mode(self._items)
		except: return None

	def MinOrNone(self) -> float | int | None:
		""" Минимальное арифметическое """
		return MinOrNone(self._items)

	def MaxOrNone(self) -> float | int | None:
		""" Максимальное арифметическое """
		return MaxOrNone(self._items)
