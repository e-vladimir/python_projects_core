# РАБОТА С ФАЙЛАМИ
# 01 ноя 2024

from os      import listdir
from os.path import isfile, join
from pathlib import Path


def FileNamesInDirectory(directory: Path) -> list[str]:
	""" Список файлов в указанной директории """
	files : list[str] = [filename for filename in listdir(directory) if isfile(join(directory, filename))]
	files.sort()

	return files
