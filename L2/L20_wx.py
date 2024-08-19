# ПАЛИТРА WX
# 18 авг 2024

import random
import wx

from   typing import Optional, List


def CopyToClipboard(in_text: str = ""):
	""" Копирование в буфер обмена """
	data = wx.TextDataObject()
	data.SetText(in_text)

	wx.TheClipboard.Open()
	wx.TheClipboard.SetData(data)
	wx.TheClipboard.Close()


# ЗАПРОСЫ
def RequestConfirm(caption: str, message: str) -> bool:
	""" Запрос подтверждения """
	return wx.MessageBox(message, caption, wx.YES_NO) == wx.YES


def RequestText(caption: str, message: str, text: str = "") -> Optional[str]:
	""" Запрос текста """
	dialog = wx.TextEntryDialog(None, message, caption, text)
	if not dialog.ShowModal() == wx.ID_OK: return None

	return dialog.GetValue()


def RequestValue(caption: str, message: str, value: int = 0) -> Optional[int]:
	""" Запрос текста """
	dialog = wx.NumberEntryDialog(None, message, "", caption, value, -999999, 999999)
	if not dialog.ShowModal() == wx.ID_OK: return None

	return dialog.GetValue()


def RequestSelect(header: str, values: List[str]) -> Optional[str]:
	""" Запрос на выбор значения из списка """
	dialog      = wx.SingleChoiceDialog(None, "", header, values)
	dialog.SetSize(wx.Size(480, 640))
	dialog.Centre()

	if not dialog.ShowModal() == wx.ID_OK: return None

	return dialog.GetStringSelection()


def ShowMessage(header: str, text: str):
	""" Отображение сообщения """
	wx.MessageBox(text, header)


def CheckPin(in_message) -> bool:
	""" Запрос и проверка PIN-кода """
	pin_raw = str(random.randint(1000, 9999))
	pin_in  = ""

	dialog = wx.TextEntryDialog(None, f"{in_message}\nPIN-код: {pin_raw}", "Запрос подтверждения")

	if dialog.ShowModal() == wx.ID_OK:
		pin_in = dialog.GetValue()

	return pin_raw == pin_in


class CApplication(wx.App):
	""" Объект: Приложение """
	def __init__(self):
		super().__init__(False)

	def OnInit(self):
		""" Инициализация приложения """
		self.InitPath()

		self.Init_00()
		self.Init_01()
		self.Init_10()
		self.Init_11()

		self.InitForms()

		return True

	def InitForms(self):
		""" Инициализация форм """
		pass

	def Init_00(self):
		""" Инициализация объектов """
		pass

	def Init_01(self):
		""" Инициализация объектов """
		pass

	def Init_10(self):
		""" Инициализация объектов """
		pass

	def Init_11(self):
		""" Инициализация объектов """
		pass

	def InitPath(self):
		""" Инициализация директорий """
		import os

		self.path_common        = f"{os.getcwd()}/"
		self.path_ui            = f"{self.path_common}ui/"

	def Start(self):
		""" Запуск приложения """
		self.MainLoop()


class CMetaPanel(wx.Panel):
	""" Объект: панель """
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.width  = 0
		self.height = 0

		self.mouse_x = 0
		self.mouse_y = 0

		self.Init_00()
		self.Init_10()
		self.InitUi()

		self.__init_events__()

	def __init_events__(self):
		self.Bind(wx.EVT_PAINT, self.__event_onPaint__)
		self.Bind(wx.EVT_MOTION, self.event_onMouseMove)

		self.InitEvents()

	def __event_onPaint__(self, event):
		self.ReadSize()

		canvas = wx.BufferedPaintDC(self)
		canvas.Clear()

		self.event_onPaint(canvas)

	def Init_00(self):
		""" Инициализация параметров """
		pass

	def Init_10(self):
		""" Инициализация объектов """
		pass

	def InitUi(self):
		""" Инициализация UI """
		pass

	def InitEvents(self):
		""" Инициализация событий """
		pass

	def event_onPaint(self, canvas: wx.BufferedPaintDC):
		pass

	def ReadSize(self):
		w, h = self.GetSize()

		self.width  = w
		self.height = h

	def event_onMouseMove(self, event: wx.MouseEvent):
		self.mouse_x = event.GetX()
		self.mouse_y = event.GetY()

	def GetTextWidth(self, canvas: wx.BufferedPaintDC, text: str):
		size = canvas.GetTextExtent(text)
		return size.GetWidth()

	def GetTextHeight(self, canvas: wx.BufferedPaintDC, text: str):
		size = canvas.GetTextExtent(text)
		return size.GetHeight()

	def DrawTextExt(self, canvas: wx.BufferedPaintDC, text: str, x: int, y: int, align_h: int = 1, align_v: int = 1):
		w    = self.GetTextWidth(canvas, text)
		h    = self.GetTextHeight(canvas, text)

		if   align_h ==  0: x -= w // 2
		elif align_h == -1: x -= w

		if   align_v ==  0: y -= h // 2
		elif align_v == -1: y -= h

		canvas.DrawText(text, x, y)

	def DrawGradientLine(self, canvas: wx.BufferedPaintDC, point0: [], point1: [], color0: wx.Colour, color1: wx.Colour, width=1, segments=4):
		r_0 = color0.Red()
		r_1 = color1.Red()

		g_0 = color0.Green()
		g_1 = color1.Green()

		b_0 = color0.Blue()
		b_1 = color1.Blue()

		k_r = (r_1 - r_0) / segments
		k_g = (g_1 - g_0) / segments
		k_b = (b_1 - b_0) / segments

		x_0 = point0[0]
		x_1 = point1[0]
		y_0 = point0[1]
		y_1 = point1[1]

		k_x = (x_1 - x_0) / (segments + 1)
		k_y = (y_1 - y_0) / (segments + 1)

		x = x_0
		y = y_0

		r = r_0
		g = g_0
		b = b_0

		for index in range(segments + 1):
			x1 = x + k_x
			y1 = y + k_y

			canvas.SetPen(wx.Pen(wx.Colour(r, g, b), width))
			canvas.DrawLine(x, y, x1, y1)

			x = x1
			y = y1

			r += k_r
			g += k_g
			b += k_b
