#!/usr/bin/env python3
#
#Download podcasts from their RSS feeds
#
# dl_podcasts v 0.1
# 

import feedparser, subprocess, shutil, os, sys
from pathlib import Path
from subprocess import Popen, PIPE, CalledProcessError


#Get settings
import settings


#Get settings
podcasts = settings.podcasts
if type(podcasts) != dict:
    print("Error: The value of 'podcast' in the settings file is not a dictionary.")
    sys.exit(1)
if len(podcasts) == 0:
    print("Error: There are no values in the 'podcast' dictionary in the settings file.")
    sys.exit(1)
pod_dir = settings.pod_dir
if os.path.isdir(pod_dir) == False:
    print("Error: Path {} not found.".format(pod_dir))
    sys.exit(1)
dl_limit = settings.dl_limit
if dl_limit == "":
    print("Error: dl_limit is empty.")
    sys.exit(1)



#Loop each podcast
for key in podcasts:
    #Parse feed
    d = feedparser.parse(podcasts[key])
    feed_file = Path(podcasts[key]).name
    pod_title = key
    pod_directory = "{}/{}".format(pod_dir, pod_title)
    #Create directory for podcast if it doesn't exists
    if os.path.isdir(pod_directory) == False:
        os.mkdir(pod_directory)
    #Save feed
    p = subprocess.Popen(['wget', '--limit-rate={}'.format(dl_limit), '-O', "{}/{}/{}".format(pod_dir, pod_title, feed_file), podcasts[key]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out,err) = p.communicate()
    if p.returncode != 0:
        print("Error: {}\n{}".format(out, err))
        sys.exit(1)
    try:
        pod_image = d.feed.image.href
    except:
        pod_image = None
    print("Running: {}\n".format(pod_title))
    #Loop episodes
    for entry in d.entries:
        ep_title = entry.title
        #Remove closing period
        if ep_title[len(ep_title) - 1:] == '.':
            ep_title = ep_title[len(ep_title)]
        ep_title = ep_title.strip().replace(' ', '_').replace(':', '-').replace('/', '-').replace(';', '-')
        #Trim long names
        if len(ep_title) > 60:
        	ep_title = ep_title[0:60]
        #Get episode image, or the podcast's image if that fails
        try:
            ep_image = entry.image.href
        except:
            if pod_image != None:
                ep_image = pod_image
            else:
                ep_image = None
        try:
            ep_year = entry.published_parsed.tm_year
            ep_year_dir = "{}/{}/{}".format(pod_dir, pod_title, ep_year)
            if os.path.isdir(ep_year_dir) == False:
                os.mkdir(ep_year_dir)
        except:
            ep_year = None
        for link in entry.links:
            if link.type == 'audio/mpeg':
                #Download 
                print(Path(link.href).name)
                mp3_file = Path(link.href).name
                cmd = ['wget', '-c', '--limit-rate={}'.format(dl_limit), '-O', "{}/{}/{}/{}{}".format(pod_dir, pod_title, ep_year, ep_title, Path(mp3_file).suffix), link.href]
                #from https://stackoverflow.com/a/28319191
                with Popen(cmd, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
                    for line in p.stdout:
                        print(line, end='')
                if p.returncode != 0:
                    raise CalledProcessError(p.returncode, p.args)

