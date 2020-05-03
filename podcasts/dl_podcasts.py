#! /usr/bin/env python3

import getpodcast
import settings

opt = getpodcast.options(
    root_dir = settings.pod_root)

for podcast in settings.podcasts:
	try:
		getpodcast.getpodcast(podcast, opt)
	except:
		print("Problem with {}".format(podcast))
		continue
