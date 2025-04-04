# ОБРАБОТЧИКИ СПИСКОВ
# 29 мар 2025

import re


def DistinctAndSortList1D(values: list, flag_distinct: bool = False, flag_sort: bool = False) -> list:
	""" Обработка списка на предмет уникальности и сортировки 1D-Списка """
	result : list = values[:]
	if     flag_distinct: result : list = list(set(values))

	if not flag_sort: return result

	return list(sorted(result))


def DistinctAndSortList2D(values: list, index_processing_item: int, flag_distinct: bool = False, flag_sort: bool = False) -> list:
	""" Обработка списка на предмет уникальности и сортировки 2D-Списка """
	try:
		result: list = values[:]

		if flag_distinct:
			filter_distinct : set[str] = set(map(lambda item: item[index_processing_item], values))
			result                     = list(filter(lambda item: item[index_processing_item] in filter_distinct, result))

		if flag_sort    :
			result                     = list(sorted(result, key=lambda item: item[index_processing_item]))

		return result
	except: return []


def DifferenceLists(list_1: list, list_2: list, flag_cmp_1_to_2: bool = False) -> list:
	""" Разница между списками """
	result = []

	# TODO: Переписать на множествах

	if flag_cmp_1_to_2:
		for item in list_1:
			if item in list_2: continue

			result.append(item)

	else:
		for item in list_2:
			if item in list_1: continue

			result.append(item)

	return result


def ClearList(items: list[str], clear_short: bool = True, clear_empty: bool = True, clear_spaces: bool = True, clear_numbers: bool = True, clear_simbols: bool = True, flag_sort: bool = True) -> list[str]:
	""" Очистка списка от пустых строк, пробелов, чисел, спецсимволов """
	result = items[:]

	if clear_numbers: result = [re.sub(r'[0-9]',                 '', item) for item in result]
	if clear_simbols: result = [re.sub(r'[^a-zA-Zа-яА-Я0-9\s.]', '', item) for item in result]
	if clear_spaces : result = [item.strip().replace('  ', ' ')            for item in result]
	if clear_empty  : result = filter(lambda item: len(item) > 0, result)
	if clear_short  : result = filter(lambda item: len(item) > 3, result)

	return sorted(result) if flag_sort else result
