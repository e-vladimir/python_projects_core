# ГЕНЕРАТОР ОТЧЁТОВ НА БАЗЕ FPDF
# 24 сен 2024

from pathlib import Path
from fpdf    import FPDF, YPos


class C30_ProcessorReportsFpdf2(FPDF):
	""" Генератор отчётов на базе FPDF """

	# Служебные методы
	def __init__(self):
		super().__init__(unit="mm", format="A4")

		self.Init_00()

	# Модель данных
	def Init_00(self):
		self._margin_l    : float = 30.0
		self._margin_r    : float = 10.0
		self._margin_t    : float = 10.0
		self._margin_b    : float = 10.0

		self._header_l    : str   = ""
		self._header_r    : str   = ""
		self._header_b    : str   = ""

		self._size_header : float = 16.0
		self._size_text   : float = 9.0
		self._size_H1     : float = 14
		self._size_H2     : float = 12
		self._size_H3     : float = 10

		self._padding_header : float = 10

	# Модель событий
	pass

	# Механика данных
	def LoadFonts(self, path_fonts: Path):
		""" Загрузка шрифтов """
		self.add_font("R",   "", f"{path_fonts.joinpath("IBM_Plex_Mono-R.ttf")}")
		self.add_font("R",  "B", f"{path_fonts.joinpath("IBM_Plex_Mono-B.ttf")}")
		self.add_font("R",  "I", f"{path_fonts.joinpath("IBM_Plex_Mono-I.ttf")}")
		self.add_font("R", "BI", f"{path_fonts.joinpath("IBM_Plex_Mono-BI.ttf")}")

	# Механика управления
	def AppendPage(self):
		""" Вставка страницы """
		self.add_page(orientation="P", format="A4")
		self.set_margins(self._margin_l, self._margin_t, self._margin_r)

		self.AppendHeader()
		self.AppendFooter()

		self.set_auto_page_break(True, self._margin_b)

	def AppendText(self):
		""" Вставка текста """
		pass

	def AppendImage(self):
		""" Вставка изображения """
		pass

	def AppendImageGrid(self):
		""" Вставка сетки изображений """
		pass

	def AppendTable(self, header: list[str], data: list[list[str]], column_sizes : list[int] = [], column_aligns: list[str] = []):
		""" Вставка таблицы данных """
		self.set_font("R", "", self._size_text)
		self.set_text_color(255, 255, 255)
		self.set_fill_color(26, 26, 26)

		cell_h_base = self._size_text * 0.35 + 1

		widths       : list[float] = [(self.w - self._margin_l - self._margin_r) / len(header)] * len(header)
		if column_sizes: widths    = [(self.w - self._margin_l - self._margin_r) * column_size / 100 for column_size in column_sizes]

		aligns       : list[str]   = ["J"] * len(header)
		if column_aligns: aligns   = column_aligns.copy()

		for column_index, header_item in enumerate(header):
			cell_w : float = widths[column_index]

			self.multi_cell(w = cell_w, h=cell_h_base, text=header_item, border=0, align=aligns[column_index], fill=True, new_y=YPos.LAST)

		self.ln()
		self.set_draw_color(200, 200, 200)
		self.set_text_color(  0,   0,   0)
		for row in data:
			cell_h_max : int = 1

			for column_index, subdata in enumerate(row):
				cell_w : float = widths[column_index]
				text_w : float = self.get_string_width(subdata)

				cell_h_max = max(cell_h_max, 1 + int(text_w // (cell_w - 1)))

			for column_index, subdata in enumerate(row):
				cell_w : float = widths[column_index]
				text_w : float = self.get_string_width(subdata)

				self.multi_cell(w=cell_w, h=cell_h_base * (cell_h_max - text_w // (cell_w - 1)), text=subdata, border="B", align=aligns[column_index], fill=False, new_y=YPos.LAST)

			self.ln()

		self.ln()

	def AppendHeader(self):
		""" Вставка верхнего колонтитула """
		if self._header_l:
			self.set_font("R", "B", self._size_header)
			self.set_xy(self._margin_l, self._margin_t)

			self.cell(text=self._header_l)

		if self._header_r:
			self.set_font("R", "B", self._size_header)
			self.set_xy(self.w - self.get_string_width(self._header_r) - self._margin_r, self._margin_t)

			self.cell(text=self._header_r)

		if self._header_b:
			self.set_font("R", "B", self._size_header * 0.75)
			self.set_xy(self._margin_l, self._margin_t + self.font_size + self.font_size * 0.75)

			self.cell(text=self._header_b)

		self.ln()

	def AppendFooter(self):
		""" Вставка нижнего колонтитула """
		pass

	def AppendH1(self, text: str):
		""" Вставка заголовка 1 """
		self.set_font("R", "B", self._size_H1)

		self.ln()
		self.ln()

		w : float = self.w
		w        -= self._margin_l
		w        -= self._margin_r

		self.multi_cell(w, text=text)
		self.ln()

	def AppendH2(self, text: str):
		""" Вставка заголовка 2 """
		self.set_font("R", "B", self._size_H2)

		self.ln()
		self.ln()

		w : float = self.w
		w        -= self._margin_l
		w        -= self._margin_r

		self.multi_cell(w, text=text)
		self.ln()

	def AppendH3(self, text: str):
		""" Вставка заголовка 3 """
		self.set_font("R", "B", self._size_H3)

		self.ln()
		self.ln()

		w : float = self.w
		w        -= self._margin_l
		w        -= self._margin_r

		self.multi_cell(w, text=text)
		self.ln()

	# Логика данных
	def ExportReportToPdf(self, file_path: Path):
		""" Экспорт отчёта в PDF-формате """
		self.output(f"{file_path}")

	# Логика управления: Страница
	def AppendTitlePage(self):
		""" Вставка титульной страницы """
		pass

	def AppendContentsPage(self):
		""" Вставка оглавления """
		pass

