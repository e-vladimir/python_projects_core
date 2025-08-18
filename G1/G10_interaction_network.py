# ВЗАИМОДЕЙСТВИЕ С СЕТЬЮ
# 18 авг 2025

import os


def CheckPing(host_or_ip: str = None) -> bool:
	""" Проверка доступности узла """
	hostname = host_or_ip or "77.88.8.1"
	response = os.system(f"ping -c 1 {hostname}")
	return response == 0
