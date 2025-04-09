import random

from   pathlib             import Path
from   PIL                 import Image

from   L3.L30_reports_fpdf import C30_ProcessorReportsFpdf2


report = C30_ProcessorReportsFpdf2()
report.info_document.title = "Тестовый документ"
report.info_document.subtitle = "Испытания генерации"
report.info_document.edition = random.randint(100, 10000)
report.LoadFonts(Path("../L0/fonts"))
report.NewPage()
report.AppendText(h1   = "Тест интеграции изображений #1",
                  text = "Форматы")
report.AppendImage("./small.png", "str")
report.AppendImage(Path("./small.png"), "Path")
report.AppendImage(Image.open("./small.png"), "Image")


report.NewPage()
report.AppendText(h1   = "Тест интеграции изображений #2",
                  text = "Изображение из файла")
report.AppendImage(Path("./small.png"), "Небольшое изображение, без ограничения по размерам")

img = Image.open(Path("./small.png"))
img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
img.save(Path("./small.png"))
report.AppendImage(Path("./small.png"), "Поворот")

img = Image.open(Path("./small.png"))
img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
img.save(Path("./small.png"))
report.AppendImage(Path("./small.png"), "Обратный поворот")

report.AppendImage(Path("./small.png"), "Небольшое изображение, 100мм по ширине", width=100)

report.AppendImage(Path("./small.png"), "Небольшое изображение, 30мм по ширине", width=30)
report.AppendImage(Path("./small.png"), "Небольшое изображение, 10мм по высоте", height=10)
report.AppendImage(Path("./big.png"),   "Большое изображение, без ограничения по размерам")
report.AppendImage(Path("./big.png"),   "Большое изображение, ограничение 100х100мм", width=100, height=100)

report.SaveToPdf(Path("./out.pdf"))
