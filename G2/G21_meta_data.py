# МЕТА-ОБЪЕКТЫ
# 18 авг 2025

from G11_conversion_data import PointToString, StringToPoint
from G20_meta_frames     import C20_MetaFrame


class C21_Coordinate2D(C20_MetaFrame):
	""" Координата """
	
	# МОДЕЛЬ ДАННЫХ
	def Init_00(self):
		super().Init_00()
		
		self._x : int = 0
		self._y : int = 0
	
	@property
	def x(self) -> int:
		return self._x
	@x.setter
	def x(self, value):
		self._x = value

	
	@property
	def y(self) -> int:
		return self._y
	@y.setter
	def y(self, value):
		self._y = value
	
	
	@property
	def xy(self) -> tuple[int, int]:
		return self.x, self.y
	@xy.setter
	def xy(self, data: tuple[int, int]):
		self.x, self.y = data
	
	# ЛОГИКА ДАННЫХ
	def ToString(self) -> str:
		""" Конвертация в строку """
		return PointToString(self.xy)

	def FromString(self, in_text: str) -> bool:
		""" Конвертация из строки """
		x, y = StringToPoint(in_text)
		
		if   x is None: return False
		elif y is None: return False
		
		self.xy = x, y
		return True
