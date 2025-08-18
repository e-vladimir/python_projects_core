# ВЗАИМОДЕЙСТВИЕ С ФАЙЛАМИ
# 18 авг 2024

from os      import listdir
from os.path import isfile, join
from pathlib import Path


def FilenamesInPath(directory: Path) -> list[str]:
	""" Список файлов по указанному пути """
	return sorted([filename for filename in listdir(directory) if isfile(join(directory, filename))])
