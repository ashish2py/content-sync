import os
import configparser

def setup_config():
	# config parser
	config = configparser.ConfigParser()
	config.read('contentsync/setup.cfg')
	
	# check current working director and set into cofig file.
	local_working_dir = os.path.dirname(os.path.abspath(__file__))
	
	if 'setup' not in config.sections():
		# writing our configuration file to 'setup.cfg'
		config.add_section("setup")
	
	config.set("setup", "path", str(local_working_dir))
	config.set("setup", "setup_type", "local")
	config.set("setup", "allow_delete", "true")
	config.set("setup", "from", "sourcedir")
	config.set("setup", "to", "targetdir")
	with open('contentsync/setup.cfg', 'w') as configfile:
		config.write(configfile)


def setup():
	setup_config()