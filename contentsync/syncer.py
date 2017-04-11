
class Sync(option):
	def __init__(self, dir1, dir2, action, **options):
		self.logger = options.get('logger', None)
		if not self.logger:
			# configure default logger to stdout
			log = logging.getLogger('dirsync')
			log.setLevel(logging.INFO)
			if not log.handlers:
				hdl = logging.StreamHandler(sys.stdout)
				hdl.setFormatter(logging.Formatter('%(message)s'))
				log.addHandler(hdl)
			self.logger = log
			
		self._dir1 = dir1
		self._dir2 = dir2

		self._copyfiles = True
		self._updatefiles = True
		self._creatdirs = True

		self._changed = []
		self._added = []
		self._deleted = []
