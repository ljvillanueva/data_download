#!/usr/bin/env python3
#
# Script to download and update playlists

import os, subprocess, sys, shutil

import settings

playlists = settings.playlists

shutil.copyfile("dl_list.sh", "{}/dl_list.sh".format(settings.dest))
os.chdir(settings.dest)

for playlist in playlists:
	try:
		p = subprocess.Popen(['bash', 'dl_list.sh', playlist], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		(out,err) = p.communicate()
		if p.returncode != 0:
			print("Error: {}\n{}".format(out, err))
			sys.exit(1)
	except:
		print("Problem with {}".format(playlist))
		continue
