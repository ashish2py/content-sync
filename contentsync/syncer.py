import os
import re
import configparser
config = configparser.ConfigParser()
config.read('contentsync/setup.cfg')
print (config.sections())

import logging

class DCMP(object):
    """Dummy object for directory comparison data storage"""
    def __init__(self, l, r, c):
        self.left_only = l
        self.right_only = r
        self.common = c


class Syncer(object):
	def __init__(self, dir1, dir2, action, **options):
		FORMAT = '%(asctime)-15s %(message)s'
		logging.basicConfig(format=FORMAT)

		self.log = logging.getLogger('dirsync')
		self.log.setLevel(logging.INFO)

		self._dir1 = dir1
		self._dir2 = dir2
		
		# options setup
		def get_option(name):
			option = config.get(name, 'default').split(',')
			option = ' '.join(option).split()
			return option
		

		self._copyfiles = True
		self._updatefiles = True
		self._creatdirs = True
				
		self._include = get_option('include')
		self._only = get_option('only')
		self._exclude = get_option('exclude')
		
		self._changed = []
		self._added = []
		self._deleted = []		
		self._ignore = []
		
		# stat vars
		self._numdirs = 0
		self._numfiles = 0
		self._numdelfiles = 0
		self._numdeldirs = 0
		self._numnewdirs = 0
		self._numupdates = 0
		self._starttime = 0.0
		self._endtime = 0.0

		# failure stat vars
		self._numcopyfld = 0
		self._numupdsfld = 0
		self._numdirsfld = 0
		self._numdelffld = 0
		self._numdeldfld = 0

	
	def check_file_permissions(self, file):
		pass
	
	def do_work(self):
		''' check accessible files and action '''
		self.log.info('working with %s and %s ' % (self._dir1, self._dir2))
		self._compare(self._dir1, self._dir2)
		return None	

	def result(self):
		''' show reports in the end '''
		self.log.info('working with %s and %s ' % (self._dir1, self._dir2))
		return None


	def _compare(self, dir1, dir2):
		""" Compare contents of two directories """
	
		left = set()
		right = set()
	
		self._numdirs += 1
				
		excl_patterns = set(self._exclude).union(self._ignore)
		
		#import ipdb;ipdb.set_trace()
		for cwd, dirs, files in os.walk(dir1):
			self._numdirs += len(dirs)
			for f in dirs + files:
				path = os.path.relpath(os.path.join(cwd, f), dir1)
				re_path = path.replace('\\', '/')
				if self._only:
					print ('only check ', self._only)
					for pattern in self._only:
						if re.match(pattern, re_path):
							# go to exclude and ignore filtering
							break
					else:
						# next item, this one does not match any pattern
						# in the _only list
						continue
	
				add_path = False
				for pattern in self._include:
					if re.match(pattern, re_path):
						add_path = True
						break
				else:
					# path was not in includes
					# test if it is in excludes
					for pattern in excl_patterns:						
						if re.match(pattern, re_path):
							# path is in excludes, do not add it
							break
					else:
						# path was not in excludes
						# it should be added
						add_path = True
	
				if add_path:
					left.add(path)
					anc_dirs = re_path[:-1].split('/')
					for i in range(1, len(anc_dirs)):
						left.add('/'.join(anc_dirs[:i]))
	
		for cwd, dirs, files in os.walk(dir2):
			for f in dirs + files:
				path = os.path.relpath(os.path.join(cwd, f), dir2)
				re_path = path.replace('\\', '/')
				for pattern in self._ignore:
					if re.match(pattern, re_path):
						if f in dirs:
							dirs.remove(f)
						break
				else:
					right.add(path)
					# no need to add the parent dirs here,
					# as there is no _only pattern detection
					if f in dirs and path not in left:
						self._numdirs += 1
	
		common = left.intersection(right)
		left.difference_update(common)
		right.difference_update(common)
		print (left, right, common)
		return DCMP(left, right, common)


