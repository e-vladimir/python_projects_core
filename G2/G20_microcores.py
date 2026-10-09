# МИКРОЯДРА
# 09 окт 2026

import enum
import json

from   dataclasses         import dataclass
from   pathlib             import Path

from   G10_datetime        import CurrentUTime
from   G11_conversion_data import UTimeToDdDmDyThTmTs
from   G20_meta_frames     import C20_MetaFrame


# КАТАЛОГИ
class EVENT_LEVELS(enum.Enum):
	""" Уровни событий """
	INFO    = ( 0, " ", "Информация")
	SUCCESS = (10, "+", "Успешно")
	WARNING = (20, "!", "Внимание")
	ERROR   = (30, "E", "Ошибка")
	
	def __init__(self, code: int, symbol: str, description: str):
		self.code        = code
		self.symbol      = symbol
		self.description = description


class PRINT_MODE(enum.IntEnum):
	""" Режим вывода """
	OFF   =  0
	SHORT = 10
	FULL  = 20
	

# ТИПЫ ДАННЫХ
@dataclass
class T20_Event:
	""" Запись события """
	details : str          = ""
	event   : str          = ""
	level   : EVENT_LEVELS = EVENT_LEVELS.INFO
	obj     : str          = ""
	utime   : int          = 0
	
	# Вывод в консоль
	def Print(self, include_object: bool = False):
		""" Вывод в консоль Время Уровень Объект Событие Детали"""
		
		time_str    = UTimeToDdDmDyThTmTs(self.utime, flag_include_thtmts=True)
		base_indent = " " * (len(time_str) + 2)
		
		if include_object:
			print(f"{time_str} [{self.level.symbol}] {self.obj}")
			print(f"{base_indent}:  {self.event}")

		else:
			print(f"{time_str} [{self.level.symbol}] {self.event}")
		
		for detail in [line.strip() for line in self.details.split('\n') if line.strip()]:
			print(f"{base_indent}.  {detail}")


# МИКРОЯДРА
class C21_MicroLogger(C20_MetaFrame):
	""" Микроядро журналирования """

	# Модель данных
	def Init_00(self):
		super().Init_00()

		self._events     : list[T20_Event] = []

		self.limit       : int             = 500
		self.print_mode  : PRINT_MODE      = PRINT_MODE.SHORT

	def SwitchPrintModeToOff(self)  : self.print_mode = PRINT_MODE.OFF
	def SwitchPrintModeToShort(self): self.print_mode = PRINT_MODE.SHORT
	def SwitchPrintModeToFull(self) : self.print_mode = PRINT_MODE.FULL

	# Модель событий
	pass

	# Механика данных
	def _AppendEvent(self, level: EVENT_LEVELS = EVENT_LEVELS.INFO, obj: str = "", event: str = "", details: str | list[str] = ""):
		""" Добавление события в журнал """
		converted_details : str = ""
		
		match details:
			case str() : converted_details = details
			case list(): converted_details = '\n'.join(details)
		
		Event = T20_Event(details = converted_details.strip(),
                          event   = event.strip(),
                          level   = level,
                          obj     = obj.strip(),
                          utime   = CurrentUTime())
		
		self._events.append(Event)
		self._events = self._events[-self.limit:]

		match self.print_mode:
			case PRINT_MODE.OFF  : return
			case PRINT_MODE.SHORT: Event.Print(include_object=False)
			case PRINT_MODE.FULL : Event.Print(include_object=True)

	def EventI(self, obj: str, event: str, details: str | list[str] = ""):
		""" Быстрое добавление записи: Информация """
		self._AppendEvent(level=EVENT_LEVELS.INFO, obj=obj, event=event, details=details)

	def EventS(self, obj: str, event: str, details: str | list[str] = ""):
		""" Быстрое добавление записи: Успешно """
		self._AppendEvent(level=EVENT_LEVELS.SUCCESS, obj=obj, event=event, details=details)

	def EventW(self, obj: str, event: str, details: str | list[str] = ""):
		""" Быстрое добавление записи: Предупреждение/Внимание """
		self._AppendEvent(level=EVENT_LEVELS.WARNING, obj=obj, event=event, details=details)

	def EventE(self, obj: str, event: str, details: str | list[str] = ""):
		""" Быстрое добавление записи: Ошибка """
		self._AppendEvent(level=EVENT_LEVELS.ERROR, obj=obj, event=event, details=details)

	def Reset(self):
		""" Очистка журнала """
		self._events.clear()

	# Механика управления
	def Print(self, skip_info: bool = False, skip_success: bool = False, skip_warning: bool = False, skip_error: bool = False):
		for Event in self._events:
			if skip_info    and Event.level == EVENT_LEVELS.INFO   : continue
			if skip_success and Event.level == EVENT_LEVELS.SUCCESS: continue
			if skip_warning and Event.level == EVENT_LEVELS.WARNING: continue
			if skip_error   and Event.level == EVENT_LEVELS.ERROR  : continue
			
			match self.print_mode:
				case PRINT_MODE.OFF  : return
				case PRINT_MODE.SHORT: Event.Print(include_object=False)
				case PRINT_MODE.FULL : Event.Print(include_object=True)
	
	# Логика данных
	pass

	# Логика управления
	pass


MicroLogger = C21_MicroLogger()


class C21_MicroConfiguration(C20_MetaFrame):
	""" Микроядро микроконфигурации """

	# Модель данных
	def Init_00(self):
		super().Init_00()
		
		self._data: dict[str, str] = dict()

	# Модель событий
	pass

	# Механика данных
	def Reset(self):
		""" Сброс данных """
		self._data.clear()
	
	# Механика управления
	pass

	# Логика данных
	def FromFile(self, file_path: Path, file_encoding: str = "utf-8", mode_append: bool = False) -> bool:
		""" Чтение данных из файла. Формат <field> = <value> """
		try   :
			with open(file_path, mode="r", encoding=file_encoding) as raw_file:
				if not mode_append: self.Reset()
				
				for raw_line in raw_file:
					if '=' not in raw_line: continue
					
					field, value = raw_line.split('=', 1)
					self._data[field.strip()] = value.strip()
				
		except Exception: return False
		
		return True
	
	def ToFile(self, file_path: Path, file_encoding: str = "utf-8") -> bool:
		""" Запись данных в файл. Формат <field> = <value> """
		try             :
			with open(file_path, mode="w", encoding=file_encoding) as file:
				for item, value in self._data.items(): file.write(f"{item} = {value}\n")
		except Exception: return False
		
		return True
	
	def FromJson(self, data: str, mode_append: bool = False) -> bool:
		""" Чтение данных из JSON строки """
		if not isinstance(data, str):             return False
		
		try   :
			parsed_data = json.loads(data)
			
			if not isinstance(parsed_data, dict): return False
			
			if not mode_append: self.Reset()
			
			for key, value in parsed_data.items():
				self._data[str(key)] = str(value)
			
			return True
		except Exception:                         return False
	
	def ToJson(self) -> str:
		""" Сериализация данных в JSON строку """
		try             : return json.dumps(self._data, ensure_ascii=False, indent=4)
		except Exception: return ""
	
	# Логика управления
	pass

	# Логика управления
	pass
