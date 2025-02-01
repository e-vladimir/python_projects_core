# УТИЛИТЫ: ГЕНЕРАТОР GL-ФАЙЛОВ И КЛАССОВ
# 01 фев 2025

import datetime
import enum

from   os      import mkdir
from   pathlib import Path


class LS(enum.Enum):
	""" Каталог L-уровней """
	def __init__(self, code: int, description: str):
		self.level       = code
		self.description = description

	L0 = ( 0, "Источник данных")
	L1 = (10, "Библиотека")
	L2 = (20, "Микроплатформа")
	L3 = (30, "Платформа")
	L4 = (40, "Модель данных")
	L5 = (50, "Модель событий")
	L6 = (60, "Механика данных")
	L7 = (70, "Механика управления")
	L8 = (80, "Логика данных")
	L9 = (90, "Логика управления")


MONTHS = ["",
          "янв",
          "фев",
          "мар",
          "апр",
          "май",
          "июн",
          "июл",
          "авг",
          "сен",
          "окт",
          "ноя",
          "дек"
          ]


baseclass   : str  = "C20_MetaFrame"    # Корневое/Родительское имя класса
classname   : str  = "ClassName"        # Имя класса
description : str  = "Описание класса"  # Описание класса
flag_item   : bool = True               # Наличие элемента класса
flag_single : bool = False              # Упаковка в едином классе

dtime              = datetime.datetime.now()
dy          : int  = dtime.year
dm          : int  = dtime.month
dd          : int  = dtime.day

# Генерация упакованного класса в одном файле
if flag_single:
	filename = f"{classname.lower()}.py"
	filepath = Path(f"./{filename}")
	if filepath.exists():
		print(f"{filename}: Файл существует, завершение.")
		exit(0)

	with open(filepath, "w") as file:
		data : list[str] = [f"# {description.upper()}",
		                    f"# {dd:02d} {MONTHS[dm].upper()} {dy}",
		                    f"\n"]

		if flag_item: data.extend([
		                    f"class C{classname}Item({baseclass}):",
		                    f"\t\"\"\"{description}.Элемент\"\"\"",
		                    f"",
		                    f"\t# {LS.L4.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L5.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L6.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L7.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L8.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L9.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    ])

		data.extend([		f"class C{classname}({baseclass}):",
		                    f"\t\"\"\"{description}\"\"\"",
		                    f"",
		                    f"\t# {LS.L4.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L5.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L6.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L7.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L8.description}",
		                    f"\tpass"
		                    f"\n"
		                    f"\n"
		                    f"\t# {LS.L9.description}",
		                    f"\tpass"
		                    ])

		file.write('\n'.join(data))
		print(f"{filename}: Генерация файла завершена.")
		exit(0)


for L in [LS.L4, LS.L5, LS.L6, LS.L7, LS.L8, LS.L9]:
	filename = f"L{L.level:02d}_{classname.lower()}.py"
	filedir  = Path(f"./L{L.level//10}")
	if not filedir.exists(): mkdir(filedir)

	filepath = Path(f"./L{L.level//10}/{filename}")
	if filepath.exists():
		print(f"{filename}: Файл существует, пропуск.")
		continue

	with open(filepath, "w") as file:
		data : list[str] = [f"# {description.upper()}: {L.description.upper()}",
		                    f"# {dd:02d} {MONTHS[dm].upper()} {dy}",
		                    f""
		                    ]

		if L.level > 40: data.extend([
							f"from L{L.level-10:02d}_{classname.lower()} import C{L.level - 10:02d}_{classname}{f", C{L.level-10:02d}_{classname}Item" if flag_item else ""}",
							"\n"
							])


		if flag_item: data.extend([
							f"class C{L.level:02d}_{classname}Item({baseclass if L.level == 40 else f"C{L.level-10:02d}_{classname}Item"}):",
		                    f"\t\"\"\"{description}.Элемент: {L.description} \"\"\"",
		                    f"\n"
		                    f"\tpass",
							f"\n"
		                    ])

		data.extend([       f"class C{L.level:02d}_{classname}({baseclass if L.level == 40 else f"C{L.level - 10:02d}_{classname}"}):",
							f"\t\"\"\"{description}: {L.description} \"\"\"",
							f"\n"
							f"\tpass"
		])

		file.write('\n'.join(data))
		print(f"{filename}: Генерация файла завершена.")
