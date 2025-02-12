# УТИЛИТЫ: ГЕНЕРАТОР GL-ФАЙЛОВ И КЛАССОВ
# 11 фев 2025

import datetime
import enum

from   dataclasses import dataclass
from os import mkdir
from   pathlib     import Path


@dataclass
class ClassInfo:
	class_name: str
	class_src : str


class META_CLASSES(ClassInfo, enum.Enum):
	C20_META_FRAME   = "C20_MetaFrame",             "G20_meta_frame"
	C30_CACTUS_FRAME = "C30_StructFrame",           "G30_cactus_frame"
	C31_CACTUS_FRAME = "C31_StructFrameWithEvents", "G31_cactus_frame"

	C20_PYSIDE_APP   = "C20_PySideApplication",     "L20_PySide6"
	C20_PYSIDE_FORM  = "C20_PySideForm",            "L20_PySide6"
	C20_PYSIDE_FRAME = "C20_DiaFrame",              "L20_PySide6"


# ПАРАМЕТРЫ ГЕНЕРАЦИИ
# Мета-класс
META_CLASS       = META_CLASSES.C20_META_FRAME

# Имя класса
CLASS_NAME        = "SomethingCalculator"

# Описание класса
CLASS_DESCRIPTION = "Калькулятор чего-то там"

# Имя файла
# Если оставить пустым, сгенерируется автоматически из имени класса
FILE_NAME         = ""

# Корневая папка генерации файлов/директорий L
DIR_ROOT          = "./"

# Генерация UI-Класса
TARGET_IS_UI      = True

# Генерация единого файла, без разделения на L4-9
TARGET_IS_SINGLE  = False


# СЛУЖЕБНЫЕ ПАРАМЕТРЫ
if not FILE_NAME: FILE_NAME = ''.join([f"_{ch}" if ch.isupper() else ch for ch in CLASS_NAME]).lower()
FILE_NAME         = FILE_NAME[1:] if FILE_NAME[0] == '_' else FILE_NAME

LEVEL             = 0
LEVELS            = [40, 50, 60, 70, 80, 90]
if TARGET_IS_UI:
	LEVELS.insert(1, 41)
	LEVELS.insert(2, 42)

DTIME             = datetime.datetime.now()
DY                = DTIME.year
DM                = DTIME.month
DD                = DTIME.day

MONTHS            = ["", "янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]


def LevelToString() -> str:
	""" Описание уровня """
	match LEVEL:
		case 40: return "Каркас UI" if TARGET_IS_UI else "Модель данных"
		case 41: return "Модель UI"
		case 42: return "Модель данных"
		case 50: return "Модель событий"
		case 60: return "Механика данных"
		case 70: return "Механика управления"
		case 80: return "Логика данных"
		case 90: return "Логика управления"
		case _ : return ""


def GenerateSingleFile():
	""" Генерация комплексного файла """
	global LEVEL

	FILE_PATH : Path      = Path(DIR_ROOT).joinpath(f"{FILE_NAME}.py")

	data      : list[str] = []
	data.append(f'# {CLASS_DESCRIPTION.upper()}')
	data.append(f'# {DD:02d} {MONTHS[DM]} {DY:04d}')
	data.append(f'')
	data.append(f'from {META_CLASS.class_src} import {META_CLASS.class_name}')
	data.append(f'')
	data.append(f'')
	data.append(f'class C_{CLASS_NAME}({META_CLASS.class_name}):')
	data.append(f'\t""" {CLASS_DESCRIPTION} """')
	data.append(f'')

	for LEVEL in LEVELS:
		data.append(f'\t# {LevelToString()}')
		data.append(f'\tpass')
		data.append(f'')

	with open(FILE_PATH.absolute(), "w") as file: file.write('\n'.join(data))


def GenerateFile():
	""" Генерация файла """
	global LEVEL

	LEVEL_PATH    : Path      = Path(DIR_ROOT).joinpath(f"L{LEVEL//10}")
	FILE_PATH     : Path      = LEVEL_PATH.joinpath(f"L{LEVEL:02d}_{FILE_NAME}.py")

	idx_level     : int       = LEVELS.index(LEVEL)
	PARENT_LEVEL  : int       = 0 if not idx_level else LEVELS[idx_level - 1]
	PARENT_CLASS  : str       = META_CLASS.class_name if not PARENT_LEVEL else f"C{PARENT_LEVEL:02d}_{CLASS_NAME}"
	PARENT_SRC    : str       = META_CLASS.class_src  if not PARENT_LEVEL else f"L{PARENT_LEVEL:02d}_{FILE_NAME}"

	data          : list[str] = []
	data.append(f'# {CLASS_DESCRIPTION.upper()}: {LevelToString().upper()}')
	data.append(f'# {DD:02d} {MONTHS[DM]} {DY:04d}')
	data.append(f'')
	data.append(f'from {PARENT_SRC} import {PARENT_CLASS}')
	data.append(f'')
	data.append(f'')
	data.append(f'class C{LEVEL:02d}_{CLASS_NAME}({PARENT_CLASS}):')
	data.append(f'\t""" {CLASS_DESCRIPTION}: {LevelToString()} """')
	data.append(f'\tpass')
	data.append(f'')

	if not LEVEL_PATH.exists(): mkdir(LEVEL_PATH)
	with open(FILE_PATH, "w") as file: file.write('\n'.join(data))


if TARGET_IS_SINGLE:
	GenerateSingleFile()
	exit(0)

for LEVEL in LEVELS:
	GenerateFile()
