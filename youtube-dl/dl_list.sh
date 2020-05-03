#!/bin/bash
# Download youtube list
#
# 

source settings.sh

#Download each file and load it to psql using osm2pgsql
for i in ${!ytlists[@]}; do
    echo ""
    echo "Working on file ${ytlists[$i]}..."
	#Download YouTube playlist videos in separate directory indexed by video order in a playlist
	youtube-dl --add-metadata --write-info-json --embed-subs --all-subs --sub-format "srt" --convert-subs srt --merge-output-format "mkv" -o $destdir'/%(playlist)s/%(playlist_index)s - %(release_date)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=${ytlists[$i]}
done
