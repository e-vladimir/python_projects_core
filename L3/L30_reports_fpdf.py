# ГЕНЕРАТОР ОТЧЁТОВ НА БАЗЕ FPDF
# 10 мар 2025

import enum

from   dataclasses import dataclass
from   datetime    import datetime
from   pathlib     import Path
from   fpdf        import Align, FPDF, FontFace, XPos, YPos
from   fpdf.enums  import TableBordersLayout, VAlign
from   fpdf.table  import Row


MONTHS_SHORT = ["", "янв", "фев", "мар", "апр", "май", "июн", "июл", "авг", "сен", "окт", "ноя", "дек"]


class BLOCKS(enum.Enum):
	""" Блоки документа """
	HEADER      = enum.auto()
	FOOTER      = enum.auto()
	H1          = enum.auto()
	H2          = enum.auto()
	H3          = enum.auto()
	TEXT        = enum.auto()
	CODE        = enum.auto()
	TABLE       = enum.auto()
	DESCRIPTION = enum.auto()


class FORMATS_PAGE(enum.StrEnum):
	""" Формат бумаги """
	A3 = "A3"
	A4 = "A4"


@dataclass
class T30_Margins:
	l: float = 100.0
	r: float = 10.0
	t: float = 15.0
	b: float = 15.0


@dataclass
class T30_InformationDocument:
	title   : str      = ""
	subtitle: str      = ""
	author  : str      = ""
	edition : int      = 1
	date    : datetime = datetime.now()


@dataclass
class T30_Color:
	r: int = 0
	g: int = 0
	b: int = 0

	def FromRGB(self, r: int, g: int = None, b: int = None):
		""" Преобразование из RGB """
		self.r = r
		self.g = g or r
		self.b = b or r

	def ToRGB(self) -> tuple[int, int, int]:
		""" Преобразование в RGB """
		return self.r, self.g, self.b

	def IsWhite(self) -> bool:
		""" Проверка белого оттенка """
		return sum(self.ToRGB()) > 759

	def IsBlack(self) -> bool:
		""" Проверка тёмного оттенка """
		return sum(self.ToRGB()) < 6


class C30_ProcessorReportsFpdf2(FPDF):
	""" Генератор отчётов на базе FPDF """

	# Служебные методы
	def __init__(self):
		super().__init__(unit="mm", format="A4")

		self.Init_00()
		self.Init_10()

	# Модель данных
	def Init_00(self):
		self._processing_h1 : str                     = ""
		self._processing_h2 : str                     = ""
		self._processing_h3 : str                     = ""

	def Init_10(self):
		self.margins_page   : T30_Margins             = T30_Margins(30, 15, 15, 15)
		self.info_document  : T30_InformationDocument = T30_InformationDocument()

	# Модель событий
	def header(self): self.AppendHeader()
	def footer(self): self.AppendFooter()

	# Механика данных
	def SwitchColors(self, block: BLOCKS):
		""" Смена цвета """
		match block:
			case BLOCKS.H1:
				self.set_text_color(  0)
				self.set_draw_color(200)
				self.set_fill_color(255)

			case BLOCKS.H2:
				self.set_text_color(  0)
				self.set_draw_color(200)
				self.set_fill_color(255)

			case BLOCKS.H3:
				self.set_text_color(  0)
				self.set_draw_color(200)
				self.set_fill_color(255)

			case BLOCKS.TEXT:
				self.set_text_color(  0)
				self.set_draw_color(200)
				self.set_fill_color(255)

			case BLOCKS.HEADER:
				self.set_text_color(150)
				self.set_draw_color(200)
				self.set_fill_color(255)

			case BLOCKS.DESCRIPTION:
				self.set_text_color(  0)
				self.set_draw_color(200)
				self.set_fill_color(255)

			case BLOCKS.TABLE:
				self.set_text_color(  0)
				self.set_draw_color(180)
				self.set_fill_color(255)

			case BLOCKS.CODE:
				self.set_text_color(  0)
				self.set_draw_color(200)
				self.set_fill_color(230)

	def SwitchFont(self, block: BLOCKS):
		""" Смена шрифта """
		match block:
			case BLOCKS.H1         : self.set_font("Sans", "B", 16)
			case BLOCKS.H2         : self.set_font("Sans", "B", 12)
			case BLOCKS.H3         : self.set_font("Sans", "B", 10)
			case BLOCKS.TEXT       : self.set_font("Sans",  "",  9)
			case BLOCKS.CODE       : self.set_font("Mono",  "",  8)
			case BLOCKS.DESCRIPTION: self.set_font("Sans", "I",  8)
			case BLOCKS.TABLE      : self.set_font("Mono",  "",  8)
			case BLOCKS.HEADER     : self.set_font("Sans",  "",  8)

	# Механика управления: Шрифты
	def LoadFonts(self, path_fonts: Path):
		""" Загрузка шрифтов """
		self.add_font("Sans",   "", f"{path_fonts.joinpath("NotoSans-Regular.ttf")}")
		self.add_font("Sans",  "B", f"{path_fonts.joinpath("NotoSans-Bold.ttf")}")
		self.add_font("Sans",  "I", f"{path_fonts.joinpath("NotoSans-Italic.ttf")}")

		self.add_font("Mono",   "", f"{path_fonts.joinpath("NotoSansMono-Regular.ttf")}")
		self.add_font("Mono",  "B", f"{path_fonts.joinpath("NotoSansMono-Bold.ttf")}")
		self.add_font("Mono",  "I", f"{path_fonts.joinpath("NotoSansMono-Regular.ttf")}")

	# Механика управления: Страница
	def NewPage(self, flag_rotate: bool = False, format_page: FORMATS_PAGE = FORMATS_PAGE.A4):
		""" Новая страница страницы """
		self.add_page(orientation = "L" if flag_rotate else "P",
		              format      = format_page.value)

		self.set_margins(self.margins_page.l, self.margins_page.t, self.margins_page.r)
		self.set_auto_page_break(True, self.margins_page.b)

	# Механика управления: Блоки
	def AppendH1(self, h1: str = ""):
		""" Добавление заголовка 1 """
		if not h1                       : return
		if     h1 == self._processing_h1: return

		self.ln(10)

		self._processing_h1 = h1

		self.SwitchFont(BLOCKS.H1)
		self.SwitchColors(BLOCKS.H1)

		self.set_x(self.margins_page.l)

		self.multi_cell(w     = 0.00,
		                align = Align.J,
		                text  = h1.upper())

	def AppendH2(self, h2: str = ""):
		""" Добавление заголовка 2 """
		if not h2                       : return
		if     h2 == self._processing_h2: return

		self.ln(5)

		self._processing_h2 = h2

		self.SwitchFont(BLOCKS.H2)
		self.SwitchColors(BLOCKS.H2)

		self.set_x(self.margins_page.l)

		self.multi_cell(w     = 0.00,
		                align = Align.J,
		                text  = h2.upper())

	def AppendH3(self, h3: str = ""):
		""" Добавление заголовка 3 """
		if not h3                       : return
		if     h3 == self._processing_h3: return

		self.ln(5)

		self._processing_h3 = h3

		self.SwitchFont(BLOCKS.H3)
		self.SwitchColors(BLOCKS.H3)

		self.set_x(self.margins_page.l)

		self.multi_cell(w     = 0.00,
		                align = Align.J,
		                text  = h3.upper())

	def AppendText(self, h1: str = "", h2: str = "", h3: str = "", text: str | list[str] = ""):
		""" Добавление текста """
		if not text: return

		self.AppendH1(h1)
		self.AppendH2(h2)
		self.AppendH3(h3)

		self.SwitchFont(BLOCKS.TEXT)
		self.SwitchColors(BLOCKS.TEXT)

		self.ln(5)

		self.set_x(self.margins_page.l)

		self.multi_cell(w     = 0.00,
		                align = Align.J,
		                text  = text if type(text) is str else '\n\n'.join(text))

	def AppendCode(self, code: str | list[str] = ""):
		""" Добавление кода """
		if not code: return

		self.SwitchFont(BLOCKS.CODE)
		self.SwitchColors(BLOCKS.CODE)

		self.ln(2)

		self.set_x(self.margins_page.l)

		self.multi_cell(w     = 0.00,
		                align = Align.J,
		                text  = code if type(code) is str else '\n\n'.join(code),
		                fill  = True,
		                padding=2)

	def AppendList(self, items: list[str], flag_numeric: bool = False):
		""" Добавление списка """
		self.SwitchFont(BLOCKS.TEXT)
		self.SwitchColors(BLOCKS.TEXT)

		self.ln(2)

		for idx, item in enumerate(items):
			marker: str = f'{idx + 1}.' if flag_numeric else '•'

			self.set_x(self.margins_page.l + 5)
			self.multi_cell(w        = 0.00,
			                align    = Align.J,
			                text     = f"{marker} {item}")
			self.ln(2)

	def AppendTable(self, description: str = "", header: list[str] = [], data: list = [], sizes: list[int] = [], aligns: list[Align] = []):
		""" Добавление таблицы """
		if not header: return
		if not data  : return

		self.ln(5)

		column_sizes  : list[float] = [(self.epw - sum(sizes)) / (len(header) - len(sizes))] * len(header)
		column_aligns : list[Align] = [Align.L] * len(header)

		for idx, size  in enumerate(sizes) : column_sizes[idx]  = size
		for idx, align in enumerate(aligns): column_aligns[idx] = align

		self.SwitchFont(BLOCKS.DESCRIPTION)
		self.SwitchColors(BLOCKS.DESCRIPTION)

		self.multi_cell(w     = 0.00,
		                text  = description,
		                align = Align.R,)

		self.SwitchFont(BLOCKS.TABLE)
		self.SwitchColors(BLOCKS.TABLE)

		self.ln(2)

		style_header = FontFace(color      =   0,
		                        fill_color = 230,
		                        emphasis   = "B")

		with self.table(headings_style  = style_header,
						col_widths      = column_sizes,
		                text_align      = column_aligns,
		                repeat_headings = True,
		                line_height     = self.font_size * 1.25,
		                padding         = 1,
		                align           = Align.R,
		                v_align         = VAlign.T,
		                borders_layout  = TableBordersLayout.HORIZONTAL_LINES) as table:
			for idx_row, data_row in enumerate([header] + data):
				row : Row = table.row()

				for data_cell in data_row:
					row.cell(data_cell)

	def AppendHeader(self):
		""" Размещение колонтитула верхнего """
		if not self.info_document.title: return

		self.set_auto_page_break(False)

		self.SwitchFont(BLOCKS.HEADER)
		self.SwitchColors(BLOCKS.HEADER)

		shift_w : int = 70
		shift_y : int =  5

		self.set_xy(self.margins_page.l, shift_y)
		self.cell(w     = self.w - shift_w - self.margins_page.l,
		          text  = f"{self.info_document.title}",
		          align = Align.L,
		          new_x = XPos.START,
		          new_y = YPos.TOP)

		self.set_xy(self.w - self.margins_page.r - shift_w, shift_y)
		self.cell(w     = shift_w,
		          text  = f"ред. {self.info_document.edition} от {self.info_document.date.day:02d} {MONTHS_SHORT[self.info_document.date.month]} {self.info_document.date.year:04d}",
		          align = Align.R,
		          new_x = XPos.START,
		          new_y = YPos.TOP)

		self.line(self.margins_page.l, shift_y + 4, self.w - self.margins_page.r, shift_y + 4)

		self.set_auto_page_break(True, self.margins_page.b)
		self.set_xy(self.margins_page.l, self.margins_page.t)

	def AppendFooter(self):
		""" Размещение колонтитула нижнего """
		shift_w : int = 70
		shift_y : int =  4

		self.set_auto_page_break(False)

		self.SwitchFont(BLOCKS.HEADER)
		self.SwitchColors(BLOCKS.HEADER)

		self.set_xy(self.margins_page.l, self.h - shift_y - 3)
		self.cell(w     = self.w - shift_w - self.margins_page.l,
		          text  = f"{self.info_document.subtitle}",
		          align = Align.L,
		          new_x = XPos.START,
		          new_y = YPos.TOP)

		self.set_xy(self.w - self.margins_page.r - shift_w, self.h - shift_y - 3)
		self.cell(w     = shift_w,
		          text  = f"стр. {self.page_no()}",
		          align = Align.R,
		          new_x = XPos.START,
		          new_y = YPos.TOP)

		self.line(self.margins_page.l, self.h - shift_y - 4, self.w - self.margins_page.r, self.h - shift_y - 4)

		self.set_auto_page_break(True, self.margins_page.b)

	# Логика данных
	def SaveToPdf(self, file_path: Path):
		""" Сохранение в PDF-файл """
		self.output(f"{file_path}")

	# Логика управления
	pass
