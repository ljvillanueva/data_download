#! /usr/bin/env python3

import getpodcast
import settings

opt = getpodcast.options(
    root_dir = settings.pod_root)

getpodcast.getpodcast(settings.podcasts, opt)
