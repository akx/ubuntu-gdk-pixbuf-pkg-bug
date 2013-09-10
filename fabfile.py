from fabric.api import *
import os
import time
from StringIO import StringIO

def _configure():
	ssh_config = {}
	with quiet():
		for line in local("vagrant ssh-config", capture=True).splitlines():
			line = line.strip().split(None, 1)
			if len(line) == 2:
				ssh_config[line[0]] = line[1]

	env.user = ssh_config["User"]
	env.hosts = ['%s:%s' % (ssh_config["HostName"], ssh_config["Port"])]
	env.key_filename = ssh_config["IdentityFile"]

_configure()

@task
def apt_proxy():
	sio = StringIO('Acquire::http { Proxy "http://192.168.11.2:3142"; };')
	put(sio, "/etc/apt/apt.conf.d/90proxy", use_sudo=True)

@task
def provision():
	packages = ["build-essential", "libgdk-pixbuf2.0-dev", "libglib2.0-dev"]
	sudo("apt-get update -y -q")
	sudo("apt-get install -y -q %s" % " ".join(packages))

@task
def fix_things():
	sudo("apt-get install shared-mime-info")

@task
def test():
	with cd("/vagrant"):
		run("rm -f test.bin")
		run("gcc -g -std=gnu99 -Wall -o test.bin test.c `pkg-config --cflags --libs glib-2.0 gdk-pixbuf-2.0`")
		run("./test.bin")