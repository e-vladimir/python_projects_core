import random
from pathlib import Path

from fpdf import Align

from L3.L30_reports_fpdf import C30_ProcessorReportsFpdf2


text = """ """

code = """<dependencies>
    <dependency>
        <groupId>ch.qos.logback</groupId>
        <artifactId>logback-classic</artifactId>
        <version>1.2.3</version>
    </dependency>
</dependencies>"""

report = C30_ProcessorReportsFpdf2()
report._info_document.title = "Тестовый документ"
report._info_document.edition = random.randint(100, 1000000)
report.LoadFonts(Path("./L0/fonts"))
report.NewPage()
report.AppendText(h1   = "Logback",
                  text = "As you already know, developers have a lot of logging tools at their disposal. In this topic, we are going to learn more about a popular logging library named Logback. It is a successor to the Log4j logging library and is based on similar concepts. Logback is fast in both synchronous and asynchronous logging and offers many useful features, which makes it a good choice for a project of any scale.")

report.AppendText(h1   = "Logback",
                  text = "The most important difference between using a Logback logger and simply printing a message to System.out is that each logger has a context. The logger context allows enabling or disabling certain log messages and is responsible for creating logger instances and arranging their hierarchy. Let's take a closer look at all these features.")

report.AppendText(h1   = "Logback",
                  h2   = "Adding Logback to a project",
                  text = ["Installing Logback is very easy – simply add the dependencies to Maven or Gradle.",
                          "To get started with Logback, you will need to add the logback-classic dependency.",
                          "If you are using Maven, open the pom.xml file and add these lines:"])

report.AppendCode("""<dependencies>
    <dependency>
        <groupId>ch.qos.logback</groupId>
        <artifactId>logback-classic</artifactId>
        <version>1.2.3</version>
    </dependency>
</dependencies>""")

report.AppendText(h1   = "Logback",
                  h2   = "Adding Logback to a project",
                  text = "If you use Gradle as your build tool, then add the following line to your build.gradle file:")

report.AppendCode("""dependencies {
    implementation ("ch.qos.logback:logback-classic:1.2.11")
}""")

report.AppendText(h1   = "Logback",
                  h2   = "Adding Logback to a project",
                  text = "This library will transitively pull two other dependencies, slf4j-api and logback-core.")

report.AppendText(h1   = "Logback",
                  h2   = "Adding Logback to a project",
                  text = "SLF4J (Simple Logging Facade for Java) is a facade or abstraction for various logging libraries, including Logback. It provides a simple logging API, and Logback implements it natively. You can invoke the SLF4J logger with Logback as its underlying implementation without any overhead.")

report.AppendText(h1   = "Logback",
                  h2   = "Basic logging",
                  text = "Let's create a class Example and declare a few Logger objects.")

report.AppendCode("""import org.slf4j.Logger
import org.slf4j.LoggerFactory

class Example {
    private val LOG_1: Logger = LoggerFactory.getLogger(Example::class.java)
    private val LOG_2: Logger = LoggerFactory.getLogger("com.example.Example")

    init {
        LOG_1.info("Information from LOG_1")
        LOG_2.warn("Warning from LOG_2")
        LOG_1.info("Are the loggers the same? {}", LOG_1 === LOG_2)
    }
}

fun main() {
    Example()
}""")

report.AppendText(text="Ма́ркер списка, бу́ллит, бу́ллет, бу́лит (англ. bullet) — типографский знак, используемый для выделения элементов списка (перечня), как показано на примере ниже:")
report.AppendList(["это первый элемент списка; обратите внимание на буллит слева;",
                   "это следующий элемент списка, и перед ним стоит ещё один буллит."])

report.AppendText(text="Источники")
report.AppendList(["Мильчин, Чельцова, 2003, 2.4.3. Знаки препинания после абзацев — элементов перечня, с. 42.",
                   "Мильчин, Чельцова, 2003, 2.4.4. Знаки препинания между элементами перечня при разном характере последних, с. 43.",
                   "ГОСТ Р 2.105-2019 Единая система конструкторской документации (ЕСКД). Общие требования к текстовым документам (Издание с Изменением N 1) - docs.cntd.ru. docs.cntd.ru. Дата обращения: 19 февраля 2024. Архивировано 19 февраля 2024 года. 6.7 Перечисления."],
                  flag_numeric=True)


report.NewPage()
report.AppendText(h1   = "Python",
                  text = "Python (в русском языке встречаются названия пито́н[15] или па́йтон[16]) — мультипарадигмальный высокоуровневый язык программирования общего назначения с динамической строгой типизацией и автоматическим управлением памятью[1][17], ориентированный на повышение производительности разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ[18]. Язык является полностью объектно-ориентированным в том плане, что всё является объектами[1]. Необычной особенностью языка является выделение блоков кода отступами[19]. Синтаксис ядра языка минималистичен, за счёт чего на практике редко возникает необходимость обращаться к документации[18]. Сам же язык известен как интерпретируемый и используется в том числе для написания скриптов[1]. Недостатками языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++[1][18].")
report.AppendTable(description = "Типы, используемые в Python",
                   header      = ["Тип", "Изменяемость", "Описание", "Примеры"],
                   data        = [["bool", "Неизменяемый", "Логический тип", "True\nFalse"],
                                  ["bytearray", "Изменяемый", "Массив байтов", "bytearray(b'Some ASCII')\nbytearray(b\"Some ASCII\")\nbytearray([119, 105, 107, 105])"],
                                  ["complex", "Неизменяемый", "Комплексное число", "3+2.7j"]],
                   sizes       = [20, 30, 30],
                   aligns      = [Align.L, Align.C, Align.C])

report.NewPage()
report.AppendText(h1="Тест таблицы",
                  h2="Короткая таблица",
                  h3="С мелкими текстами",
                  text=" ")
texts = """Адмиральский час — так с петровских времен и почти до революции назывался в Архангельске полдень.
Аксинья-полузимница — 24 января старого стиля. По народному календарю середина зимы, уже прошла половина холодов.
Аред — мифическая личность, упоминаемая в Библии, достопамятная удивительным своим долголетием.
Аредовы веки — народное русское выражение удивительного долголетия, равнозначно с "Мафусаиловы годы".
Афанасьев день — 18 января старого стиля. С этого дня кончается полярная ночь, в полдень показываются утренние зори. Со 2 февраля старого стиля появляется солнце, светлое время увеличивается с каждыми сутками, постепенно переходя в беззакатный северный трехмесячный день."""

header = ["Термин", "Описание\Определение"]
data   = texts.split('\n')
for idx, row in enumerate(data): data[idx] = row.split(' — ')

report.AppendTable(description = "Словарь поморских и специальных слов и выражений,\nобъяснение собственных имен и названий",
                   header=header,
                   data=data,
                   sizes=[50],
                   aligns=[Align.R, Align.J])

report.AppendText(h1="Тест таблицы",
                  h2="Короткая таблица",
                  h3="С длинными текстами",
                  text=" ")

header = ["ЯП", "Краткое описание"]
data   = [["Компилируемые и Интерпретируемые", "Компилируемые: С, С++, Pascal\nИнтерпретируемые: Visual Basic Script (VBScript), JavaScript, Python, PHP\nУсловно компилируемые: C# и остальные языки .Net, Java для Java-машины\n\nЛюбая программа на языке программирования это прежде всего текст. Текст понятен человеку, и сравнительно легко может быть обработан компьютером, потому что буквы и другие текстовые символы в компьютере представлены некими целыми числами, их еще называют кодами символов. Программа, которая обрабатывает текст на языке программирования и создает по нему последовательность команд микропроцессора называется компилятор. То есть компилятор переводит числа, которые человек воспринимает как текст в другие числа, которые компьютер воспринимает как команды микропроцессора.\n\nЯзыки, для которых требуется компилятор, называются компилируемыми. Чтобы запустить такую программу, мало просто написать ее. Надо еще прогнать ее через компилятор, получить исполняемый модуль, например, в операционной системе Windows это файл с расширением .exe, и только после этого запустить его на выполнение.\n\nТакая схема, конечно, не всех устраивала и программисты придумали языки, которым не требуется компилятор. Для таких языков перевод текста в команды микропроцессора происходит незаметно сразу после запуска текстовой программы. Правда, для этого текстовая программа должна запускаться под управлением другой уже готовой программы, которая называется Интерпретатор. Интерпретатор и делает эту незаметную компиляцию. Языки для которых требуется интерпретатор назвали Интерпретируемыми.\n\nГлавное отличие компилируемых языков от интерпретируемых в скорости выполнения программ. Считается, что программы написанные на компилируемых языках выполняются быстрее чем на интерпретируемых. Но сам процесс написания и тестирования интерпретируемой программы проходит проще, так как нет необходимости в промежуточном шаге компиляции.\n\nДля некоторых языков, таких как С#, компиляция проходит особым образом в два этапа. Дело в том, что в среде .Net программа на C# после компиляции становится не набором команд микропроцессора, а преобразуется в программу на еще одном промежуточном языке CIL — Common Intermediate Language, (ранее называвшийся MSIL — Microsoft Intermediate Language), которая для запуска передается на вход Just-In-Time (JIT) компилятору .Net. Такая последовательность преобразований из одного языка в другой позволяет не заботиться о типе микропроцессора установленного в компьютере и дает большую универсальность для работы программ.\n\nПохожим образом, программа на TypeScript сначала компилируется в текстовую программу, или, как говорят, в код на JavaScript, который затем уже может быть выполнен интерпретатором JavaScript. Такое усложнение позволяет воспользоваться преимуществами строгой типизации данных и отловом ошибок на этапе компиляции, которые доступны в TypeScript."],
          ["Универсальные и специализированные", "Классификация говорит сама за себя. Есть языки, на которых можно в принципе написать любую программу, но не всегда это можно сделать, например, быстро. Или такая программа не обязательно будет оптимально быстро работать. Типичный универсальный язык всех времен и народов: С++. И в этом его большой плюс. А, может, даже два плюса )).\n\nСпециализация в языках программирования касается, как правило, либо предметной области, например, математические вычисления (Fortran, F#), искусственный интеллект (LISP), веб-разработка (PERL, PHP), компьютерные игры (Unity, Lua), бухгалтерия (1С) и т.д., либо какой-то технологии программирования, например, многопоточность как в языке Cи-Омега (Cw) или способ записи операторов как в F#.\n\nДля разных областей приложений создаются свои языки или скрипты. Особенно это относится к компьютерным играм, в которых переплетаются сразу несколько видов искусства, науки и технологии. Но системы разработки игр также используют и уже известные языки, например, Python в системе нарративных игр Ren’Py или язык Swift для устройств Apple."],
          ["Алгоритмические и Языки описания данных", "Алгоритмические языки, конечно, тоже умеют описывать данные, но в основном предназначены для создания больших и сложных программ, которые описывают действия, то есть алгоритмы.\n\nЯзыки же описания данных предназначены только для описания данных для разных типов приложений. Эти языки можно считать необходимой нагрузкой к обычным алгоритмическим языкам. Например, если вы учите JavaScript для разработки веб-приложений, то скорее всего вам придется также изучить и синтаксис каскадных таблиц стилей CSS и язык описания данных JSON, в формате которого удобно передавать данные между веб-сервером и клиентом.\n\nИли, например, язык работы с базами данных SQL, по сути является языком для обработки и получения данных, но также включает в себя раздел Data Definition Language или Язык Описания Данных.\n\nВообще, на способы описания и управления данными сейчас разработчикам приходится обращать внимания, пожалуй, не меньше чем на описание алгоритмов."],
          ["Низкоуровневые и Высокоуровневые", "Этот тип классификации, хоть и немного теряет актуальность, поскольку подавляющее большинство языков теперь можно отнести к высокоуровневым, но все еще имеет место, поскольку низкоуровневые языки существуют.\n\nЭта классификация была актуальна на заре развития компьютеров, когда число доступных компиляторов можно было пересчитать по пальцам, а написать, например, драйвер клавиатуры на Ассемблере можно было в качестве развлечения в свободное время.\n\nНапомню, что Ассемблер, это язык, команды которого максимально соответствуют командам самого микропроцессора, которые позволяют обрабатывать данные размером один, два или четыре байта, за счет чего представить на нем сложные типы данных очень и очень проблематично. Но зато по скорости выполнения программ языку Ассемблера просто нет равных.\n\nЯзык CIL, который уже упоминался выше, это в некотором смысле аналог ассемблера, но для системы .Net. Команды CIL преобразуются JIT-компилятором .Net в наборы инструкций микропроцессора в зависимости от типа самого микропроцессора, на котором установлен .Net. Как правило, программа на CIL это результат компиляции программы написанной на одном из языков высокого уровня .Net.\n\nКроме того, CIL это особый язык. Писать программу непосредственно на нем может оказаться слишком долго. Программы на этом языке генерируются компиляторами и используются программным обеспечением платформы .Net. Поэтому он считается языком программирования скорее для машины чем для человека."],
          ["Объектно-Ориентированные и Структурные языки программирования", "Появление объектно-ориентированного программирования, сокращенно ООП, примерно со второй половины 80-х годов 20-го века стало настоящей технологической революцией. Это был буквально переворот, сейчас объясню почему. До ООП были популярны языки структурного программирования. И программисты были вполне счастливы писать программы на структурных языках высокого уровня, потому что в свое время это тоже было колоссальным шагом вперед.\n\nДело в том, что компьютер удалось создать только после титанических усилий таких гениев как Алан Тьюринг, который разработал свою теорию — машину Тьюринга, на основе которой и работают все числовые компьютеры в наши дни. Принцип машины Тьюринга, вкратце, состоит в том, что в оперативной памяти записана последовательность команд микропроцессора, в том числе команд условных или безусловных переходов на другие команды. Эти переходы на ассемблере называются JMP (англ.: jump — прыжок, переход), а в языках высокого уровня обозначаются командой GOTO (англ.: go to — перейти к чему-л.).\n\nДля программирования компьютера первоначально существовал язык Ассемблер, команды которого почти один в один соответствуют командам микропроцессора. Теоретически, на Ассемблере можно написать любую программу, но практически перенос абстракций прикладных задач на него совсем не простое дело.\n\nДля программирования прикладных задач, примерно с начала 70-х годов 20-го века и появилось структурное программирование, для создания которого потребовались усилия других гениев, таких как Никлаус Вирт, создатель языка Паскаль и Эдсгер Дейкстра, который первым написал о необходимости избавляться от оператора GOTO в языках высокого уровня и предложил решение как это сделать с помощью трех типов операторов и функций.\n\nНа практике это вылилось в появление языков программирования, таких как Basic, С, Паскаль, Algol, Cobol, Fortran, PL1. Разработка программ методом «сверху вниз» в структурном программировании превратилась в сплошное удовольствие. Суть ее состояла в написании набора функций, содержащих подфункции, которые можно вызывать, подставляя на вход нужные данные и получая соответствующий результат.\n\nТаким образом, в языках структурного программирования алгоритмы на основе функций стоят как бы на первом месте, а данные для них можно брать откуда угодно. Не последнюю роль в этом сыграла идея автора кибернетики Норберта Винера о функции как о черном ящике, на вход которому можно подавать любые данные и наблюдать получаемый выход.\n\nДля небольших задач типа сортировки данных или нахождения кратчайшего пути структурное программирование подходило идеально. Были найдены решения для большинства сложных алгоритмических задач. Появились фундаментальные труды, такие как многотомник “Искусство программирования” Дональда Кнута, который до сих пор считается настольной книгой для программистов.\n\nОднако, увеличение сложности программ в результате привело к появлению и бо́льших шансов на внесение ошибок в программы, так как возможность подставлять любые данные на вход процедурам и функциям влекло за собой побочные эффекты. Так, например, в 1999 году космический аппарат NASA «Mars Climate Orbiter» потерпел крушение в из-за ошибки в программе — подстановки неправильных данных.\n\nВ результате появилась новая концепция объектно-ориентированного программирования, в котором во главу угла ставится, как я его называю, принцип актуальности данных, а функции становятся как бы приложением к данным, которые они должны обрабатывать. Объект это, в первую очередь, набор данных со своими функциями. В ООП вводятся ограничения на доступ функций к «чужим» данным, что уменьшает возможность непреднамеренного изменения данных и резко повышает надежность программ.\n\nПосле появления объектно-ориентированных языков программирования, таких как С++, Object Pascal, Java, С#, а также новых аппаратных возможностей компьютеров, объемы программ и данных для них увеличились многократно, если не на порядки, что легко оценить хотя бы по объемам дистрибутивов программ, которые перестали помещаться сначала на дискеты, а потом и на компакт диски. А программирование снова как бы встало с головы на ноги."]]
report.AppendTable(description = "Языки программирования",
                   header=header,
                   data=data,
                   sizes=[50],
                   aligns=[Align.L, Align.J])

report.SaveToPdf(Path("./out.pdf"))
