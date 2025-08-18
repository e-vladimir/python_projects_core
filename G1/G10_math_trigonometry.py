# МАТЕМАТИКА: ТРИГОНОМЕТРИЯ
# 18 авг 2025

# Y=^ X=<>

import math

from   typing import Union


def CalcDistanceByPoints(in_point_0: Union[list, tuple], in_point_1: Union[list, tuple]):
	""" Вычисление расстояния между 2мя точками """
	if len(in_point_0) != 2: return None
	if len(in_point_1) != 2: return None

	dx = in_point_1[0] - in_point_0[0]
	dy = in_point_1[1] - in_point_0[1]

	return math.hypot(dx, dy)
