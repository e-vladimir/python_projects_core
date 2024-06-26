# РАБОТА С ФАЙЛАМИ
# 08 июн 2024

from os      import listdir
from os.path import isfile, join
from pathlib import Path


def FileNamesInDirectory(directory: Path) -> list[str]:
	""" Список файлов в указанной директории """
	return [filename for filename in listdir(directory) if isfile(join(directory, filename))]
