from contentsync import setup
from contentsync.syncer import Syncer


def init_setup():
	setup()
	
source_dir = '/Users/Ashish/Documents/workspace/zaya/projects/content-sync/contentsync/sourcedir/'
target_dir = '/Users/Ashish/Documents/workspace/zaya/projects/content-sync/contentsync/sourcedir/'

def sync(sourcedir, targetdir, action, **options):
	# copier
	copier = Syncer(sourcedir, targetdir, action, **options)
	copier.do_work()

	# print report at the end
	# copier.report()

	
if __name__ == '__main__':
	init_setup()
	sync(source_dir, target_dir, 'sync')