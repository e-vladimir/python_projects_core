# БИБЛИОТЕКА: ОБОЛОЧКА СИСТЕМЫ
# 2023-09-20

import os
import subprocess

from   typing import List


def ExecSingleCmdInShell(cmd: str) -> str:
    """ Выполнение команды в системной оболочке """
    return os.popen(cmd).read()


def ExecMultipleCmdInShell(cmds: List[str]) -> List[str]:
    """  """
    result : List[str] = []
    for cmd in cmds: result.extend(subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).communicate()[0].decode("utf-8").split('\n'))

    return result
