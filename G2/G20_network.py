# КОМПОНЕНТЫ СЕТИ
# 2024-06-02

from socketserver import StreamRequestHandler, ThreadingTCPServer


class CBaseServer:
	""" Базовый сервер """

	def __init__(self):
		self.Init_00()
		self.Init_10()

	# Модель данных
	def Init_00(self):
		""" Инициализация параметров """
		self._lock_enable : bool = False
		self._state_bind  : bool = False

		self._net_mask    : str  = "0.0.0.0"
		self._net_port    : int  = 20000

	def Init_10(self):
		""" Инициализация объектов """
		pass

	# Модель событий
	pass

	# Механика данных
	def LockEnable(self, flag: bool = None) -> bool:
		""" Блокировка доступности сервера """
		if flag is None: return self._lock_enable
		else           :        self._lock_enable = flag

	def StateBind(self, flag: bool = None) -> bool:
		""" Состояние Bind """
		if flag is None: return self._state_bind
		else           :        self._state_bind = flag

	def NetMask(self, ip: str = None) -> str:
		""" Маска сети """
		if ip is None: return self._net_mask
		else         :        self._net_mask = ip

	def NetPort(self, port: int = None) -> int:
		""" Порт сети """
		if port is None: return self._net_port
		else           :        self._net_port = port

	# Механика управления
	pass

	# Логика данных
	pass

	# Логика управления
	pass


class CTcpSessionIncome(StreamRequestHandler):
	""" TCP-Сессия входящая """
	def handle(self):
		print("Входящее соединение")


class CTcpSessionOutcome:
	""" TCP-Сессия исходящая """

	# Модель данных
	pass

	# Модель событий
	pass

	# Механика данных
	pass

	# Механика управления
	pass

	# Логика данных
	pass

	# Логика управления
	pass


class CUdpSessionIncome:
	""" UDP-Сессия входящая """
	pass


class C20_TcpServer(CBaseServer, ThreadingTCPServer):
	""" TCP-Сервер """

	def __init__(self, net_mask: str = "0.0.0.0", net_port: int = 20000):
		CBaseServer.__init__(self)

		self.NetMask(net_mask)
		self.NetPort(net_port)

	# Модель данных
	pass

	# Механика данных
	def EnableServer(self):
		""" Включение сервера """
		if self.LockEnable(): return
		if self.StateBind() : return

		try   :
			ThreadingTCPServer.__init__(self, (self.NetMask(), self.NetPort()), CTcpSessionIncome, False)

			self.server_bind()
			self.server_activate()

			self.StateBind(True)

			self.serve_forever()
		except: pass

	def DisableServer(self):
		""" Отключение сервера """
		try   :
			self.shutdown()
			self.server_close()

			self.StateBind(False)
		except: pass

	# Механика управления
	pass

	# Логика данных
	pass

	# Логика управления
	pass


class C20_UdpServer(CBaseServer):
	""" UDP-Сервер """
	pass
