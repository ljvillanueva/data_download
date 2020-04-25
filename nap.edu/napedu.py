#!/usr/bin/env python3
#

import feedparser, os, subprocess, sys

dest = "/mnt/raid/nap/"

feeds = ['http://feeds.nap.edu/nap/new/topic/276', 'http://feeds.nap.edu/nap/new/topic/277','http://feeds.nap.edu/nap/new/topic/292','http://feeds.nap.edu/nap/new/topic/278','http://feeds.nap.edu/nap/new/topic/279','http://feeds.nap.edu/nap/new/topic/280','http://feeds.nap.edu/nap/new/topic/281','http://feeds.nap.edu/nap/new/topic/282','http://feeds.nap.edu/nap/new/topic/283','http://feeds.nap.edu/nap/new/topic/284','http://feeds.nap.edu/nap/new/topic/285','http://feeds.nap.edu/nap/new/topic/286','http://feeds.nap.edu/nap/new/topic/287','http://feeds.nap.edu/nap/new/topic/288','http://feeds.nap.edu/nap/new/topic/289','http://feeds.nap.edu/nap/new/topic/290','http://feeds.nap.edu/nap/new/topic/423','http://feeds.nap.edu/nap/new/topic/293','http://feeds.nap.edu/nap/new/topic/478','http://feeds.nap.edu/nap/new/topic/294']


for feed in feeds:
	d = feedparser.parse(feed)
	print("Running: {}".format(d.feed.title_detail['value']))
	(title, category) = d.feed.title_detail['value'].split("|")
	title = title.strip()
	category = category.strip()
	os.chdir(dest)
	if os.path.isdir(category) == False:
		os.mkdir(category)
	for entry in d.entries:
		book_title = entry.title_detail['value']
		entry_link = entry.link.split("/")
		book_link = entry_link[len(entry_link) - 1]
		book_file = "{category}/{book_title}.{year}.pdf".format(category = category, book_title = book_title, year = entry['published_parsed'][0])
		book_url = "https://download.nap.edu/cart/download.cgi?record_id={book_link}".format(book_link = book_link)
		if os.path.exists(book_file) == False:
			print("Downloading: {}".format(book_title))
			p = subprocess.Popen(['wget', '-O', book_file, '--load-cookies', 'cookies.txt', book_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			(out,err) = p.communicate()
			if p.returncode != 0:
				print("Error: {}\n{}".format(out, err))
				sys.exit(1)
		else:
			print("Skipping: {}".format(book_title))

