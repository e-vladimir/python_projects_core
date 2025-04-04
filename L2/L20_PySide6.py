# ПАКЕТ ДЛЯ РАБОТЫ С PYSIDE-6
# 04 апр 2025

import enum

from   pathlib           import  Path
from   PySide6           import  QtGui
from   PySide6.QtCore    import (Qt,
                                 QModelIndex,
                                 Signal)
from   PySide6.QtGui     import (QColor,
	                             QFont,
	                             QIcon,
	                             QKeyEvent,
	                             QMouseEvent,
	                             QPainter,
	                             QStandardItem,
	                             QStandardItemModel,
	                             QTextCursor)
from   PySide6.QtWidgets import (QApplication,
	                             QDialog,
	                             QDialogButtonBox,
	                             QFileDialog,
	                             QFormLayout,
	                             QGroupBox,
	                             QInputDialog,
	                             QLabel,
	                             QLineEdit,
	                             QListWidget,
	                             QListWidgetItem,
	                             QMainWindow,
	                             QMessageBox,
	                             QPlainTextEdit,
	                             QWidget)


class ROLES(enum.IntEnum):
	TEXT              = Qt.ItemDataRole.DisplayRole
	IDO               = 100
	IDP               = 101
	FILENAME          = 102
	GROUP             = 103
	VISUAL_STYLE_CELL = 200
	VISUAL_STYLE_ROW  = 201
	SORT_INDEX        = 300


class VISUAL_STYLE(enum.StrEnum):
	H1        = "H1"
	H2        = "H2"
	H3        = "H3"

	SEPARATOR = "SEP"

	BOLD      = "B"
	UNDERLINE = "U"
	ITALIC    = "I"

	ALIGN_R   = "R"
	ALIGN_L   = "L"
	ALIGN_C   = "C"


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

		self.on_Inited()

	def Init_00(self):
		""" Инициализация параметров """
		self._path_common : Path = Path()
		self._path_ui     : Path = Path()

	def Init_01(self):
		""" Инициализация директорий """
		self._path_common : Path = Path.cwd()
		self._path_ui     : Path = self._path_common / "ui"

	def Init_10(self)   : pass
	def Init_11(self)   : pass
	def Init_12(self)   : pass
	def Init_20(self)   : pass

	# СИСТЕМНЫЕ СОБЫТИЯ
	def on_Inited(self):
		""" Событие: При инициализации """

	def on_Start(self):
		""" Событие: При запуске приложения """
		pass

	# СИСТЕМНЫЕ МЕТОДЫ
	def Start(self):
		""" Запуск приложения """
		self.on_Start()
		self.exec_()

	def Close(self):
		""" Завершение приложения """
		self.quit()


# ИНСТРУМЕНТАРИЙ ФОРМ
class C20_PySideForm(QMainWindow):
	def __init__(self, application: C20_PySideApplication, *args, **kwargs):
		super().__init__(None)

		self.Application = application

		self.InitUi()

		self.Init_00()
		self.Init_01()

		self.Init_10()
		self.Init_11()
		self.Init_12()

		self.Init_20()

		self.InitMenus()
		self.InitEvents()

		self.on_Inited()

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
		shift_width  : int = QApplication.primaryScreen().availableGeometry().width()  - self.width()
		shift_height : int = QApplication.primaryScreen().availableGeometry().height() - self.height()

		self.move(shift_width // 2, shift_height // 2)

	# СЛУЖЕБНЫЕ МЕТОДЫ
	def InitUi(self):
		""" Инициализация UI для генератора из QtDesigner """
		pass

	def Close(self):
		""" Закрытие формы """
		self.on_RequestClose()
		self.close()
		self.on_Closed()

	def Open(self):
		""" Открытие формы """
		self.on_RequestOpen()

		if not self.isMaximized(): self.MoveToCenter()

		self.show()

		self.on_Opened()

	def show(self):
		super().show()

		self.on_Showed()

	def UpdateData(self):
		""" Обновление данных """
		self.on_RequestUpdateData()

	def PartialUpdateData(self):
		""" Обновление данных (частичное) """
		self.on_RequestPartialUpdateData()

	# СИСТЕМНЫЕ СОБЫТИЯ
	def closeEvent(self, event: QtGui.QCloseEvent) -> None:
		""" Системное событие закрытия формы """
		self.on_RequestClose()

		super().closeEvent(event)

	def resizeEvent(self, event):
		""" Изменение размера окна """
		super().resizeEvent(event)

		self.on_Resize()

	# СЛУЖЕБНЫЕ СОБЫТИЯ
	def on_Inited(self)                  : pass
	def on_RequestOpen(self)             : pass
	def on_Opened(self)                  : pass
	def on_Showed(self)                  : pass
	def on_RequestClose(self)            : pass
	def on_Closed(self)                  : pass
	def on_RequestUpdateData(self)       : pass
	def on_RequestPartialUpdateData(self): pass
	def on_Resize(self)                  : pass


# UI-Компоненты
class C20_DiaFrame(QWidget):
	""" UI-компонент область отрисовки """

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.Init_00()
		self.Init_01()
		self.Init_10()
		self.Init_11()
		self.Init_20()

	def Init_00(self): pass
	def Init_01(self): pass
	def Init_10(self): pass
	def Init_11(self): pass
	def Init_20(self): pass

	def DrawBackground(self, painter: QPainter):
		pass

	def DrawBorder(self, painter: QPainter):
		pass

	def paintEvent(self, event):
		painter = QPainter(self)

		self.DrawBackground(painter)
		self.DrawBorder(painter)


class C20_ActiveLabel(QLabel):
	""" Label с реакцией на клик """

	clicked        = Signal()
	wheelMovedUp   = Signal()
	wheelMovedDown = Signal()

	def mouseReleaseEvent(self, ev: QMouseEvent):
		super().mouseReleaseEvent(ev)

		match ev.button():
			case Qt.MouseButton.LeftButton: self.clicked.emit()

	def wheelEvent(self, event):
		try   :
			if   event.angleDelta().y() < 0: self.wheelMovedDown.emit()
			elif event.angleDelta().y() > 0: self.wheelMovedUp.emit()
		except: pass
		super().wheelEvent(event)


class C20_ActiveGroupBox(QGroupBox):
	""" GroupBox с реакцией на клик """

	clicked = Signal()

	def mouseReleaseEvent(self, ev: QMouseEvent):
		super().mouseReleaseEvent(ev)

		match ev.button():
			case Qt.MouseButton.LeftButton: self.clicked.emit()


class C20_PlainTextEditWithCompleter(QPlainTextEdit):
	""" Текстовое поле ввода с поддержкой автодополнения """
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self._raw_dictionary : list[str] = []
		self._dictionary     : list[str] = []

		self._text_cursor   = self.textCursor()

	@property
	def dictionary(self) -> list[str]:
		return sorted(self._raw_dictionary)

	@dictionary.setter
	def dictionary(self, words: list[str]):
		self._raw_dictionary = ' '.join(filter(lambda word: len(word) > 3, words)).replace(' ', ' ').split(' ')
		self._dictionary     = sorted([word.lower() for word in self._raw_dictionary])

	def _requestComplete(self):
		self._text_cursor.select(QTextCursor.SelectionType.WordUnderCursor)
		selected_text = self._text_cursor.selectedText().lower()

		if len(selected_text) >= 3:
			for item in self._dictionary:
				if selected_text not in item: continue

				pos = self._text_cursor.position()

				self._text_cursor.setPosition(pos)
				self._text_cursor.insertText(item[len(selected_text):])
				self._text_cursor.setPosition(pos)
				self._text_cursor.setPosition(pos + len(item) - len(selected_text), QTextCursor.MoveMode.KeepAnchor)

				self.setTextCursor(self._text_cursor)

				break

	def _requestApplyComplete(self) -> bool:
		if not self.textCursor().selection().toPlainText().strip(): return False

		self._text_cursor.setPosition(self._text_cursor.selectionEnd())
		self._text_cursor.insertText(' ')
		self.setTextCursor(self._text_cursor)

		return True

	def keyPressEvent(self, event: QKeyEvent) -> None:
		if event.key() == Qt.Key.Key_Return:
			if self._requestApplyComplete(): return

		super().keyPressEvent(event)

		match event.key():
			case Qt.Key.Key_Backspace: return
			case Qt.Key.Key_Control  : return
			case Qt.Key.Key_Copy     : return
			case Qt.Key.Key_Down     : return
			case Qt.Key.Key_F1       : return
			case Qt.Key.Key_F10      : return
			case Qt.Key.Key_F11      : return
			case Qt.Key.Key_F12      : return
			case Qt.Key.Key_F2       : return
			case Qt.Key.Key_F3       : return
			case Qt.Key.Key_F4       : return
			case Qt.Key.Key_F5       : return
			case Qt.Key.Key_F6       : return
			case Qt.Key.Key_F7       : return
			case Qt.Key.Key_F8       : return
			case Qt.Key.Key_F9       : return
			case Qt.Key.Key_Left     : return
			case Qt.Key.Key_Paste    : return
			case Qt.Key.Key_Return   : return
			case Qt.Key.Key_Right    : return
			case Qt.Key.Key_Shift    : return
			case Qt.Key.Key_Space    : return
			case Qt.Key.Key_Up       : return

			case _                   : self._requestComplete()


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
	def __init__(self,  title, message, items: list[str] | dict[str, QIcon], parent=None, items_checked: list[str] = []):
		super().__init__(parent)

		self.setWindowTitle(title)

		layout_form    = QFormLayout(self)
		layout_form.addRow(QLabel(message))

		self.list_items   = QListWidget()

		match items:
			case list():
				for item in items:
					item_text = QListWidgetItem()
					item_text.setText(item)
					item_text.setCheckState(Qt.CheckState.Unchecked if item not in items_checked else Qt.CheckState.Checked)

					self.list_items.addItem(item_text)

			case dict():
				for text, icon in items.items():
					item_text = QListWidgetItem()
					item_text.setIcon(icon)
					item_text.setText(text)
					item_text.setCheckState(Qt.CheckState.Unchecked if text not in items_checked else Qt.CheckState.Checked)

					self.list_items.addItem(item_text)


		layout_form.addRow(self.list_items)

		btn_box     = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, Qt.Orientation.Horizontal, self)
		layout_form.addRow(btn_box)

		btn_box.accepted.connect(self.accept)
		btn_box.rejected.connect(self.reject)

	def selectedItems(self) -> list[str]:
		result : list[str] = []

		for index_row in range(self.list_items.count()):
			item_text : QListWidgetItem = self.list_items.item(index_row)
			if item_text.checkState() == Qt.CheckState.Unchecked: continue

			result.append(item_text.data(Qt.ItemDataRole.DisplayRole))

		return result


class QItemsInputDialog(QDialog):
	def __init__(self,  title, message, items: list[str] | dict[str, QIcon], parent=None):
		super().__init__(parent)

		self.setWindowTitle(title)

		layout_form     = QFormLayout(self)
		layout_form.addRow(QLabel(message))

		self.list_items = QListWidget()

		match items:
			case list():
				for text in items:
					item_text = QListWidgetItem()
					item_text.setText(text)

					self.list_items.addItem(item_text)

			case dict():
				for text, icon in items.items():
					item_text = QListWidgetItem()
					item_text.setIcon(icon)
					item_text.setText(text)

					self.list_items.addItem(item_text)

		layout_form.addRow(self.list_items)

		btn_box         = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, Qt.Orientation.Horizontal, self)
		layout_form.addRow(btn_box)

		btn_box.accepted.connect(self.accept)
		btn_box.rejected.connect(self.reject)

	def selectedItem(self) -> str | None:
		return self.list_items.currentItem().data(Qt.ItemDataRole.DisplayRole)


class QFindReplaceTextDialog(QDialog):
	def __init__(self,  title, message, text_find: str = "", text_replace: str = "", parent=None):
		super().__init__(parent)

		self.setMinimumWidth(480)

		self.setWindowTitle(title)

		layout_form       = QFormLayout(self)
		layout_form.addRow(QLabel(message))

		self.edit_find    = QLineEdit()
		self.edit_find.setText(text_find)

		self.edit_replace = QLineEdit()
		self.edit_replace.setText(text_replace)

		layout_form.addRow(QLabel("Фрагмент поиска"))
		layout_form.addRow(self.edit_find)

		layout_form.addRow(QLabel("Фрагмент замены"))
		layout_form.addRow(self.edit_replace)

		btn_box           = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, Qt.Orientation.Horizontal, self)
		layout_form.addRow(btn_box)

		btn_box.accepted.connect(self.accept)
		btn_box.rejected.connect(self.reject)

	def textFind(self) -> str:
		""" Фрагмент поиска """
		return self.edit_find.text()

	def textReplace(self) -> str:
		""" Фрагмент замены """
		return self.edit_replace.text()


class QMultipleTextInputDialog(QDialog):
	def __init__(self, title, message, items: list[any], parent=None, dictionary : list[str] = []):
		super().__init__(parent)

		self.setWindowTitle(title)
		self.setMinimumWidth(480)
		self.setMinimumHeight(360)

		layout_form    = QFormLayout(self)
		layout_form.addRow(QLabel(message))

		self.edit_text   = C20_PlainTextEditWithCompleter()
		self.edit_text.dictionary = dictionary
		self.edit_text.setPlainText('\n'.join(items))

		layout_form.addRow(self.edit_text)

		btn_box     = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel, Qt.Orientation.Horizontal, self)
		layout_form.addRow(btn_box)

		btn_box.accepted.connect(self.accept)
		btn_box.rejected.connect(self.reject)

	def textValues(self) -> list[str]:
		""" Список строк  """
		return self.edit_text.toPlainText().split('\n')


def RequestText(title: str, message: str, old_text: str = "", items: list[str] | None = None) -> None | str:
	""" Запрос текста """
	dialog = QInputDialog(None)
	dialog.setWindowTitle(title)
	dialog.setLabelText(message)
	dialog.resize(480, 150)

	if items is not None:
		dialog.setComboBoxItems(items)
		dialog.setComboBoxEditable(True)

	dialog.setTextValue(old_text)

	if not dialog.exec_(): return None
	return dialog.textValue()


def RequestMultipleText(title: str, message: str, old_text: list[str] = [], dictionary: list[str] = []) -> None | list[str]:
	""" Запрос многострочного текста """
	dialog = QMultipleTextInputDialog(title, message, old_text, None, dictionary)

	if not dialog.exec_(): return None
	return dialog.textValues()


def RequestValue(title: str, message: str, value_old: int | float = None, value_min: int | float = None, value_max: int | float = None) -> None | int | float:
	""" Запрос числового значения """
	dialog = QInputDialog(None)
	dialog.setWindowTitle(title)
	dialog.setLabelText(message)
	dialog.resize(480, 150)

	if   type(value_min) is int  : dialog.setIntMinimum(value_min)
	elif type(value_min) is float: dialog.setDoubleMinimum(value_min)

	if   type(value_max) is int  : dialog.setIntMaximum(value_max)
	elif type(value_max) is float: dialog.setDoubleMaximum(value_max)

	if   type(value_old) is int  : dialog.setIntValue(value_old)
	elif type(value_old) is float: dialog.setDoubleValue(value_old)

	if not dialog.exec_(): return None

	if   type(value_old) is int  : return dialog.intValue()
	elif type(value_old) is float: return dialog.doubleValue()


def RequestConfirm(title: str, message: str, flag_btn_cancel: bool = False) -> bool | None:
	""" Запрос подтверждения """
	if flag_btn_cancel: btns = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel
	else              : btns = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No

	result = QMessageBox(QMessageBox.Icon.Question, title, message, btns).exec_()

	if result  == QMessageBox.StandardButton.Cancel: return None
	return result == QMessageBox.StandardButton.Yes


def RequestItem(title: str, message: str, items: list[str] | dict[str, QIcon]) -> str | None:
	""" Запрос значения из списка """
	if not items               : return None

	dialog_items     = QItemsInputDialog(title, message, items)

	match items:
		case list(): max_length : int = max(list(map(len, items)))
		case dict(): max_length : int = max(list(map(len, items.keys())))
		case _     : max_length : int = 480

	size_w     : int = min(480, max_length * 15)
	size_w           = max(360, size_w)
	size_h     : int = min(640, len(items) * 40)
	size_h           = max(240, size_h)

	dialog_items.resize(size_w, size_h)

	if not dialog_items.exec_(): return None

	return dialog_items.selectedItem()


def RequestItems(title: str, message: str, items: list[str], items_checked: list[str] | dict[str, QIcon] = []) -> list[str] | None:
	""" Запрос значений из списка """
	if not items               : return None
	
	max_length : int = max(list(map(len, items)))
	size_w     : int = min(480, max_length * 15)
	size_w           = max(360, size_w)
	size_h     : int = min(640, len(items) * 55)
	size_h           = max(240, size_h)

	dialog_items     = QMultipleItemsInputDialog(title, message, items, items_checked=items_checked)
	dialog_items.resize(size_w, size_h)

	if not dialog_items.exec_(): return None

	return dialog_items.selectedItems()


def RequestFilepath(title: str, filename: str = "", filters: str = "") -> Path | None:
	""" Запрос файла """
	dialog_filepath = QFileDialog()
	filepath, filemask = dialog_filepath.getOpenFileName(None, title, filename, filters)

	if not filepath: return None

	return Path(filepath)


def RequestDirectory(title: str, current_dir: str = "") -> Path | None:
	""" Запрос директории """
	dialog          = QFileDialog()
	dialog.setFileMode(QFileDialog.FileMode.Directory)
	dialog.setOption(QFileDialog.Option.ShowDirsOnly)
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


def FindItemFromStandardModelByData(model: QStandardItemModel, text: str, role=Qt.ItemDataRole.DisplayRole) -> QStandardItem | None:
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
		else                   : index_item : QModelIndex = model.index(index_row, 0, parent_index)

		result.append(index_item)
		result.extend(IndexesFromStandardModel(model, index_item))

	return result


def FindIndexFromStandardModelByData(model: QStandardItemModel, text: str, role=Qt.ItemDataRole.DisplayRole) -> QModelIndex | None:
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

		result = super().setData(index, value, role)

		if   role == Qt.ItemDataRole.DisplayRole:
			self.dataChanged.emit()

		elif role == Qt.ItemDataRole.UserRole   :
			self.dataChanged.emit()

		elif role == Qt.ItemDataRole.CheckStateRole:
			if value == Qt.CheckState.Checked.value : self.itemChecked.emit()
			else                                    : self.itemUnchecked.emit()

		return result

	# Инструментарий
	def removeAll(self):
		""" Удаление всех данных из модели """
		self.removeRows(0, self.rowCount())

	def checkIdo(self, ido: str) -> bool:
		""" Проверка наличия данных с указанным IDO """
		return self.indexByData(ido, ROLES.IDO) is not None

	# Инструментарий отображения
	def setRowColor(self, parent: QStandardItem, row: int, color_bg: QColor = Qt.GlobalColor.transparent, color_fg: QColor = Qt.GlobalColor.black):
		""" Установка цвета строки """
		for index_col in range(self.columnCount()):
			item_child : QStandardItem | None = parent.child(row, index_col)
			if item_child is None: continue

			item_child.setBackground(color_bg)
			item_child.setForeground(color_fg)

	def setColColor(self, parent: QStandardItem, col: int, color_bg: QColor = Qt.GlobalColor.white, color_fg: QColor = Qt.GlobalColor.black):
		""" Установка цвета колонки """
		for index_row in range(self.rowCount()):
			item_child : QStandardItem | None = parent.child(index_row, col)
			if item_child is None: continue

			item_child.setBackground(color_bg)
			item_child.setForeground(color_fg)

	def setCellColor(self, parent: QStandardItem, row: int, col: int, color_bg: QColor = Qt.GlobalColor.white, color_fg: QColor = Qt.GlobalColor.black):
		""" Установка цвета ячейки """
		item_child: QStandardItem | None = parent.child(row, col)
		if item_child is None: return

		item_child.setBackground(color_bg)
		item_child.setForeground(color_fg)

	def setRowBold(self, parent: QStandardItem, row: int, flag: bool = True):
		""" Установка шрифта строки Жирный """
		for index_col in range(self.columnCount()):
			item_child : QStandardItem | None = parent.child(row, index_col)
			if item_child is None: continue

			font_item  : QFont                = item_child.font()
			font_item.setBold(flag)

			item_child.setFont(font_item)

	def adjustGroupView(self, flag_only_top: bool = True, flag_setup_h: bool = True, flag_apply_bg: bool = False):
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
	def indexes(self, parent: QModelIndex = None) -> list[QModelIndex]:
		""" Список всех индексов в колонке 0 """
		if parent is None: return IndexesFromStandardModel(self)
		else             : return [self.index(idx_row, 0, parent) for idx_row in range(self.rowCount(parent))]

	def indexByData(self, text: str, role : Qt.ItemDataRole | ROLES = Qt.ItemDataRole.DisplayRole) -> QModelIndex | None:
		""" Поиск индекса по данным """
		return FindIndexFromStandardModelByData(self, text, role)

	def itemByData(self, text: str, role : Qt.ItemDataRole | ROLES = Qt.ItemDataRole.DisplayRole) -> QStandardItem | None:
		""" Поиск элемента по данным """
		index_data = self.indexByData(text, role)
		if index_data is None: return None

		return self.itemFromIndex(index_data)

	def dataByCheckState(self, role : Qt.ItemDataRole | ROLES = Qt.ItemDataRole.DisplayRole, check_state = Qt.CheckState.Checked) -> list:
		""" Выборка данных для выбранных элементов """
		result = []

		for index_data in self.indexes():
			item_data = self.itemFromIndex(index_data)

			if not item_data.checkState() == check_state: continue

			result.append(item_data.data(role))

		return result

	def indexesInRowByIdo(self, ido: str) -> list[QModelIndex]:
		""" Индексы в строке с указанным IDO """
		result       : list[QModelIndex]  = []

		index_row    : QModelIndex | None = self.indexByData(ido, ROLES.IDO)
		if index_row is None: return result

		index_parent : QModelIndex        = index_row.parent()

		for index_col in range(self.columnCount()):
			result.append(self.index(index_row.row(), index_col, index_parent))

		return result

	# Инструменты
	def fastAppendRow(self, label_labels : str | list[str]):
		""" Быстрое добавление строк """
		data  : list[str]              = []

		if   type(label_labels) is str : data.append(label_labels)
		elif type(label_labels) is list: data = label_labels

		items : list[C20_StandardItem] = []

		for label in data: items.append(C20_StandardItem(label))

		self.appendRow(items)

	def fastAppendLabels(self, labels: list[str], col_count: int = 2):
		""" Быстрое создание таблицы """
		for label in labels:
			data = [label] + [""] * col_count

			self.fastAppendRow(data)


class C20_StandardItem(QStandardItem):
	def __init__(self, title: str, data = "", data_role : int | ROLES = ROLES.IDO, flag_align_right : bool = False, flag_bold: bool = False, flag_checked : bool = None):
		"""  """
		super().__init__()

		self.setText(title)
		self.setData(data, data_role)

		font : QFont = self.font()
		font.setBold(flag_bold)

		if flag_align_right: self.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
		if flag_bold       : self.setFont(font)

		if flag_checked is not None:
			self.setCheckable(True)
			self.setCheckState(Qt.CheckState.Checked if flag_checked else Qt.CheckState.Unchecked)
