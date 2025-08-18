# ГЕНЕРАЦИЯ
# 18 авг 2025

import time
import random


def GenerateId() -> str:
	""" Генератор ID """
	_time = time.time()
	return f"{int(_time * 1000000)}-{random.randint(10, 1000):04d}{random.randint(10, 1000):04d}"


def GenerateOctetId() -> str:
	""" Генератор Октет ID """
	_time = f"{int(time.time() * 10000000):02X}"
	return '-'.join([_time[2:6],
	                 _time[6:10],
	                 _time[10:14]])
