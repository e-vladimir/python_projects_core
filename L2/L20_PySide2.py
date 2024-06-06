# ПАКЕТ ДЛЯ РАБОТЫ С PySide-2
# 2024-04-22

from pathlib           import Path
from PySide2           import QtGui
from PySide2.QtCore    import (Qt,
                               QModelIndex,
                               Signal)
from PySide2.QtGui     import (QStandardItemModel,
                               QStandardItem,
                               QPainter,
                               QColor,
                               QFont)
from PySide2.QtWidgets import (QApplication,
                               QDesktopWidget,
                               QFileDialog,
                               QInputDialog,
                               QMainWindow,
                               QMessageBox,
                               QWidget,
                               QDialog,
                               QFormLayout,
                               QLabel,
                               QDialogButtonBox,
                               QListWidget,
                               QListWidgetItem,
                               QPlainTextEdit)


ROLE_OID : int = 100


# ИНСТРУМЕНТАРИЙ ПРИЛОЖЕНИЯ
class C20_PySideApplication(QApplication):
	def __init__(self):
		super().__init__()

		self.Init_00()
		self.Init_01()

		self.Init_10()
		self.Init_11()
		self.Init_12()

		self.Init_20()

		self.on_Init()

	def Init_00(self):
		""" Инициализация параметров """
		self._path_common : Path = Path()
		self._path_ui     : Path = Path()

	def Init_01(self):
		""" Инициализация директорий """
		self._path_common : Path = Path.cwd()
		self._path_ui     : Path = Path.joinpath(self._path_common, "ui")

	def Init_10(self)   : pass
	def Init_11(self)   : pass
	def Init_12(self)   : pass
	def Init_20(self)   : pass

	# СИСТЕМНЫЕ СОБЫТИЯ
	def on_Init(self):
		""" Событие: При инициализации """

	def on_Start(self):
		""" Событие: При запуске приложения """
		pass

	# СИСТЕМНЫЕ МЕТОДЫ
	def Start(self):
		""" Запуск приложения """
		self.on_Start()
		self.exec_()


# ИНСТРУМЕНТАРИЙ ФОРМ
class C20_PySideForm(QMainWindow):
	def __init__(self, application: C20_PySideApplication, *args, **kwargs):
		super().__init__(None)

		self.application = application

		self.InitUi()

		self.Init_00()
		self.Init_01()

		self.Init_10()
		self.Init_11()
		self.Init_12()

		self.Init_20()

		self.InitMenus()
		self.InitEvents()

		self.on_Init()

	def Init_00(self)    : pass
	def Init_01(self)    : pass
	def Init_10(self)    : pass
	def Init_11(self)    : pass
	def Init_12(self)    : pass
	def Init_20(self)    : pass

	def InitMenus(self) : pass
	def InitEvents(self): pass

	def MoveToCenter(self):
		""" Центрирование окна на мониторе """
		shift_width  : int = QDesktopWidget().width()  - self.width()
		shift_height : int = QDesktopWidget().height() - self.height()

		self.move(shift_width // 2, shift_height // 2)

	# СЛУЖЕБНЫЕ МЕТОДЫ
	def InitUi(self):
		""" Инициализация UI для генератора из QtDesigner """
		pass

	def Close(self):
		""" Закрытие формы """
		self.on_Close()
		self.close()

	def Open(self):
		""" Открытие формы """
		self.on_Open()

		if not self.isMaximized(): self.MoveToCenter()

		self.show()

	def show(self):
		super().show()

		self.on_Show()

	def UpdateData(self):
		""" Обновление данных """
		self.on_UpdateData()

	def UpdateDataPartial(self):
		""" Обновление данных (частичное) """
		self.on_UpdateDataPartial()

	# СИСТЕМНЫЕ СОБЫТИЯ
	def closeEvent(self, event: QtGui.QCloseEvent) -> None:
		""" Системное событие закрытия формы """
		self.on_Close()

		super().closeEvent(event)

	def resizeEvent(self, event):
		""" Изменение размера окна """
		super().resizeEvent(event)

		self.on_Resize()

	# СЛУЖЕБНЫЕ СОБЫТИЯ
	def on_Close(self)            : pass
	def on_Init(self)             : pass
	def on_Open(self)             : pass
	def on_Show(self)             : pass
	def on_UpdateData(self)       : pass
	def on_UpdateDataPartial(self): pass
	def on_Resize(self): pass


# UI-Компоненты
class C20_DiaFrame(QWidget):
	""" UI-компонент диаграмма """
	def DrawBackground(self, painter: QPainter):
		pass

	def DrawBorder(self, painter: QPainter):
		pass

	def paintEvent(self, event):
		painter = QPainter(self)

		self.DrawBackground(painter)

		self.DrawBorder(painter)


# ИНСТРУМЕНТАРИЙ СООБЩЕНИЙ
def ShowMessage(title: str, message: str, description: str = ""):
	""" Показать простое текстовое сообщение """
	dialog = QMessageBox()
	dialog.setWindowTitle(title)
	dialog.setText(message)
	dialog.setDetailedText(description)

	dialog.exec_()


# ИНСТРУМЕНТАРИЙ ЗАПРОСОВ
class QMultipleItemsInputDialog(QDialog):
	def __init__(self,  title, message, items: list[any], parent=None):
		super().__init__(parent)

		self.setWindowTitle(title)

		layout_form    = QFormLayout(self)
		layout_form.addRow(QLabel(message))

		self.list_items   = QListWidget()

		for item in items:
			item_text = QListWidgetItem()
			item_text.setText(item)
			item_text.setCheckState(Qt.Unchecked)

			self.list_items.addItem(item_text)

		layout_form.addRow(self.list_items)

		btn_box     = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		layout_form.addRow(btn_box)

		btn_box.accepted.connect(self.accept)
		btn_box.rejected.connect(self.reject)

	def itemsSelected(self) -> list[str]:
		result : list[str] = []

		for index_row in range(self.list_items.count()):
			item_text : QListWidgetItem = self.list_items.item(index_row)
			if item_text.checkState() == Qt.Unchecked: continue

			result.append(item_text.text())

		return result


class QMultipleTextInputDialog(QDialog):
	def __init__(self,  title, message, items: list[any], parent=None):
		super().__init__(parent)

		self.setWindowTitle(title)
		self.setMinimumWidth(480)
		self.setMinimumHeight(360)

		layout_form    = QFormLayout(self)
		layout_form.addRow(QLabel(message))

		self.edit_text   = QPlainTextEdit()
		self.edit_text.setPlainText('\n'.join(items))
		layout_form.addRow(self.edit_text)

		btn_box     = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		layout_form.addRow(btn_box)

		btn_box.accepted.connect(self.accept)
		btn_box.rejected.connect(self.reject)

	def textValues(self) -> list[str]:
		"""  """
		return self.edit_text.toPlainText().split('\n')


def RequestText(title: str, message: str, old_text: str = "") -> None | str:
	""" Запрос текста """
	dialog = QInputDialog(None)
	dialog.setWindowTitle(title)
	dialog.setLabelText(message)
	dialog.resize(480, 150)
	dialog.setTextValue(old_text)

	if not dialog.exec_(): return None
	return dialog.textValue()


def RequestMultipleText(title: str, message: str, old_text: list[str] = []) -> None | list[str]:
	""" Запрос многострочного текста """
	dialog = QMultipleTextInputDialog(title, message, old_text)

	if not dialog.exec_(): return None
	return dialog.textValues()


def RequestValue(title: str, message: str, old_value: int | float = None, min: int | float = None, max: int | float = None) -> None | int | float:
	""" Запрос числового значения """
	dialog = QInputDialog(None)
	dialog.setWindowTitle(title)
	dialog.setLabelText(message)
	dialog.resize(480, 150)

	if   type(min) is int  : dialog.setIntMinimum(min)
	elif type(min) is float: dialog.setDoubleMinimum(min)

	if   type(max) is int  : dialog.setIntMaximum(max)
	elif type(max) is float: dialog.setDoubleMaximum(max)

	if   type(old_value) is int  : dialog.setIntValue(old_value)
	elif type(old_value) is float: dialog.setDoubleValue(old_value)

	if not dialog.exec_(): return None
	if   type(old_value) is int  : return dialog.intValue()
	elif type(old_value) is float: return dialog.doubleValue()


def RequestConfirm(title: str, message: str, flag_btn_cancel: bool = False) -> bool | None:
	""" Запрос подтверждения """
	if flag_btn_cancel: btns = QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
	else              : btns = QMessageBox.Yes | QMessageBox.No

	result = QMessageBox(QMessageBox.Question, title, message, btns).exec_()

	if result  == QMessageBox.Cancel: return None
	return result == QMessageBox.Yes


def RequestItem(title: str, message: str, items: list[str]) -> str | None:
	""" Запрос значения из списка """
	if not items               : return None

	dialog_items     = QInputDialog(None)
	dialog_items.setWindowTitle(title)
	dialog_items.setLabelText(message)
	dialog_items.setComboBoxItems(items)
	dialog_items.setOption(dialog_items.UseListViewForComboBoxItems, True)

	max_length : int = max(list(map(len, items)))

	size_w     : int = min(480, max_length * 15)
	size_h     : int = min(640, len(items) * 55)

	dialog_items.resize(size_w, size_h)

	if not dialog_items.exec_(): return None

	return dialog_items.textValue()


def RequestItems(title: str, message: str, items: list[str]) -> list[str] | None:
	""" Запрос значений из списка """
	if not items               : return None
	
	max_length : int = max(list(map(len, items)))
	size_w     : int = min(480, max_length * 15)
	size_h     : int = min(640, len(items) * 55)

	dialog_items     = QMultipleItemsInputDialog(title, message, items)
	dialog_items.resize(size_w, size_h)

	if not dialog_items.exec_(): return None

	return dialog_items.itemsSelected()


def RequestFilepath(title: str, filename: str = "", filters: str = "") -> Path | None:
	""" Запрос файла """
	dialog_filepath = QFileDialog()
	filepath, filemask = dialog_filepath.getOpenFileName(None, title, filename, filters)

	if not filepath: return None

	return Path(filepath)


def RequestDirectory(title: str, current_dir: str = "") -> Path | None:
	""" Запрос директории """
	dialog          = QFileDialog()
	dialog.setFileMode(QFileDialog.Directory)
	dialog.setOption(QFileDialog.ShowDirsOnly)
	dialog.setDirectory(current_dir)

	directory : str = dialog.getExistingDirectory(None, title)

	if not directory: return None

	return Path(directory)


# ИНСТРУМЕНТАРИЙ МОДЕЛЕЙ
def ItemsFromStandardModel(model: QStandardItemModel, parent_item: QStandardItem | None = None) -> list[QStandardItem]:
	""" Получение списка элементов  """
	result : list[QStandardItem] = []

	if parent_item is None: parent_item = model.invisibleRootItem()

	for index_row in range(parent_item.rowCount()):
		subitem : QStandardItem = parent_item.child(index_row, 0)
		if subitem is None: continue

		result.append(subitem)

		result.extend(ItemsFromStandardModel(model, subitem))

	return result


def FindItemFromStandardModelByData(model: QStandardItemModel, text: str, role=Qt.DisplayRole) -> QStandardItem | None:
	""" Поиск элемента модели по тексту """
	for item in ItemsFromStandardModel(model):
		if item.data(role) == text: return item

	return None


def IndexesFromStandardModel(model: QStandardItemModel, parent_index: QModelIndex | None = None) -> list[QModelIndex]:
	""" Список индексов из модели """
	result : list[QModelIndex] = []

	if parent_index is None: count_row = model.rowCount()
	else                   : count_row = model.rowCount(parent_index)

	for index_row in range(count_row):
		if parent_index is None: index_item : QModelIndex = model.index(index_row, 0)
		else                   : index_item : QModelIndex = parent_index.child(index_row, 0)

		result.append(index_item)
		result.extend(IndexesFromStandardModel(model, index_item))

	return result


def FindIndexFromStandardModelByData(model: QStandardItemModel, text: str, role=Qt.DisplayRole) -> QModelIndex | None:
	""" Поиск элемента модели по тексту """
	for index_item in IndexesFromStandardModel(model):
		if index_item.data(role) == text: return index_item

	return None


# МОДЕЛИ
class C20_StandardItemModel(QStandardItemModel):
	""" Расширение стандартной модели данных """

	textChanged      = Signal()
	dataChanged      = Signal()

	itemChecked      = Signal()
	itemUnchecked    = Signal()

	index_processing = QModelIndex()

	# Расширение функций
	def setData(self, index, value, role=None):
		""" Перезапись служебного метода """
		self.index_processing = index

		if   role == Qt.DisplayRole:
			self.textChanged.emit()

		elif role == Qt.UserRole   :
			self.dataChanged.emit()

		elif role == Qt.CheckStateRole:
			if value == Qt.Checked : self.itemChecked.emit()
			else                   : self.itemUnchecked.emit()

		return super().setData(index, value, role)

	# Инструментарий
	def removeAll(self):
		""" Удаление всех данных из модели """
		self.removeRows(0, self.rowCount())

	# Инструментарий отображения
	def setRowColor(self, parent: QStandardItem, row: int, color_bg: QColor = Qt.white, color_fg: QColor = Qt.black):
		""" Установка цвета строки """
		for index_col in range(self.columnCount()):
			item_child : QStandardItem | None = parent.child(row, index_col)
			if item_child is None: continue

			item_child.setBackground(color_bg)
			item_child.setForeground(color_fg)

	def setCellColor(self, parent: QStandardItem, row: int, col: int, color_bg: QColor = Qt.white, color_fg: QColor = Qt.black):
		""" Установка цвета ячейки """
		item_child: QStandardItem | None = parent.child(row, col)
		if item_child is None: return

		item_child.setBackground(color_bg)
		item_child.setForeground(color_fg)

	def setRowBold(self, parent: QStandardItem, row: int):
		""" Установка шрифта строки Жирный """
		for index_col in range(self.columnCount()):
			item_child : QStandardItem | None = parent.child(row, index_col)
			if item_child is None: continue

			font_item  : QFont                = item_child.font()
			font_item.setBold(True)

			item_child.setFont(font_item)

	def setGroupsView(self, flag_only_top: bool = True, flag_setup_h: bool = True, flag_apply_bg: bool = False):
		""" Настройка отображения групп """
		color_bg_top = QColor(220, 220, 220)
		color_bg     = QColor(235, 235, 235)
		color_fg     = QColor(  0,   0,   0)

		for index_item in self.indexes():
			item_model  : QStandardItem = self.itemFromIndex(index_item)

			flag_top    : bool          = item_model.parent() is None
			flag_group  : bool          = item_model.rowCount() > 0

			if not flag_group                : continue
			if not flag_top and flag_only_top: continue

			font_item   : QFont         = item_model.font()
			font_item.setBold(flag_top)
			font_item.setUnderline((not flag_top) and (not flag_apply_bg))

			item_model.setFont(font_item)

			if flag_apply_bg:
				item_model.setBackground(color_bg_top if flag_top else color_bg)
				item_model.setForeground(color_fg)

			if not flag_setup_h: continue

			index_row   : int                  = index_item.row()
			item_parent : QStandardItem | None = item_model.parent()
			if item_parent is None: item_parent = self.invisibleRootItem()

			for index_col in range(1, self.columnCount()):
				item_model : QStandardItem | None = item_parent.child(index_row, index_col)
				if item_model is None: continue

				item_model.setFont(font_item)

				if flag_apply_bg:
					item_model.setBackground(color_bg_top if flag_top else color_bg)
					item_model.setForeground(color_fg)

	# Выборки данных
	def indexes(self) -> list[QModelIndex]:
		""" Список всех индексов в колонке 0 """
		return IndexesFromStandardModel(self)

	def indexByData(self, text: str, role=Qt.DisplayRole) -> QModelIndex | None:
		""" Поиск индекса по данным """
		return FindIndexFromStandardModelByData(self, text, role)

	def itemByData(self, text: str, role = Qt.DisplayRole) -> QStandardItem | None:
		""" Поиск элемента по данным """
		index_data = self.indexByData(text, role)
		if index_data is None: return None

		return self.itemFromIndex(index_data)


class C20_StandardItem(QStandardItem):
	def __init__(self, title: str, data = "", data_role : int = ROLE_OID, flag_align_right : bool = False, flag_bold: bool = False, flag_checked : bool = None):
		"""  """
		super().__init__()

		self.setText(title)
		self.setData(data, data_role)

		font : QFont = self.font()
		font.setBold(flag_bold)

		if flag_align_right: self.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
		if flag_bold       : self.setFont(font)

		if flag_checked is not None:
			self.setCheckable(True)
			self.setCheckState(Qt.Checked if flag_checked else Qt.Unchecked)
