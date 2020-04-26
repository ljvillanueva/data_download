#!/usr/bin/env python3
#
# Download NYTimes front covers
# https://static01.nyt.com/images/YYYY/MM/DD/nytfrontpage/scannat.pdf

import os, datetime, wget
 
#Adapted from https://www.pythonprogramming.in/get-range-of-dates-between-specified-start-and-end-date.html
first = datetime.datetime.strptime("2012-07-06", "%Y-%m-%d")
current = datetime.datetime.today()
date_array = (first + datetime.timedelta(days=x) for x in range(0, (current-first).days))

os.mkdir("nytimes")

for date_object in date_array:
	cover_url = date_object.strftime("https://static01.nyt.com/images/%Y/%m/%d/nytfrontpage/scannat.pdf")
	year_dir = date_object.strftime("%Y")
	file_date = date_object.strftime("%Y-%m-%d")
	if os.path.isdir("nytimes/{}".format(year_dir)) == False:
		os.mkdir("nytimes/{}".format(year_dir))
	print("\nDownloading {} to {}\n".format(cover_url, "nytimes/{}/{}.pdf".format(year_dir, file_date)))
	try:
		wget.download(cover_url, "nytimes/{}/{}.pdf".format(year_dir, file_date))
	except:
		continue

