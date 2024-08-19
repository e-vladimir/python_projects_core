# ТАЙМЕРЫ
# 18 авг 2024

import threading
import time

from   typing import Callable


class C20_ThreadTimer(threading.Thread):
	""" Многопоточный таймер """

	def __init__(self, target: Callable, interval_sec: float, flag_enable: bool = False):
		self.Init_00()
		self.Init_10()

		self.IntervalSec(interval_sec)

		if flag_enable: self.EnableTimer()

		super().__init__(target=target, daemon=True)

		self.start()

	# Служебные уровни инициализации
	def Init_00(self):
		self._lock_processing : bool            = True
		self._interval_sec    : float           = 1.000

	def Init_10(self):
		self._target          : Callable | None = None

	# Модель данных
	pass

	# Модель событий
	pass

	# Механика данных
	def IntervalSec(self, value: float = None) -> float:
		""" Интервал обработки (в секундах) """
		if value is None: return self._interval_sec
		else            :        self._interval_sec = value

	def EnableLockProcessing(self):
		""" Включение блокировки обработки """
		self._lock_processing = True

	def DisableLockProcessing(self):
		""" Отключение блокировки обработки """
		self._lock_processing = False

	# Механика управления
	def ControlProcessing(self):
		""" Контроль обработки """
		if self._lock_processing: return
		if self._target is None : return

		self.on_RequestProcessing()

	# Логика данных
	def EnableTimer(self):
		""" Включение таймера """
		self.DisableLockProcessing()

	def DisableTimer(self):
		""" Отключение таймера """
		self.EnableLockProcessing()

	def run(self):
		while True:
			time.sleep(self._interval_sec)

			self.ControlProcessing()

	# Логика управления
	def on_RequestProcessing(self):
		""" Запрос на начало вызова """
		self._target()
