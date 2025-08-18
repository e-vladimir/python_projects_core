# ТАЙМЕРЫ
# 18 авг 2024

import threading
import time

from   typing import Callable


class C20_ThreadTimer(threading.Thread):
	""" Многопоточный таймер """

	def __init__(self, target: Callable, interval_ts: float, flag_enable: bool = False):
		self.Init_00()
		self.Init_10()

		self.interval = interval_ts

		if flag_enable: self.EnableTimer()

		super().__init__(target=target, daemon=True)

		self.start()

	# Модель данных
	def Init_00(self):
		self._lock_processing : bool            = True
		self._interval_ts     : float           = 1.000

	def Init_10(self):
		self._target          : Callable | None = None

	@property
	def interval(self) -> float:
		return self._interval_ts
	@interval.setter
	def interval(self, ts: float):
		self._interval_ts = max(0.001, ts)


	@property
	def lock_processing(self) -> bool:
		return self._lock_processing
	@lock_processing.setter
	def lock_processing(self, flag: bool):
		self._lock_processing = flag

	# Механика управления
	def ControlProcessing(self):
		""" Контроль обработки """
		if self._lock_processing: return
		if self._target is None : return

		self.on_RequestProcessing()

	# Логика данных
	def EnableTimer(self):
		""" Включение таймера """
		self.lock_processing = False

	def DisableTimer(self):
		""" Отключение таймера """
		self.lock_processing = True

	def run(self):
		while True:
			time.sleep(self._interval_ts)

			self.ControlProcessing()

	# Логика управления
	def on_RequestProcessing(self):
		""" Запрос на начало вызова """
		if self._target is None: return

		self._target()
