#!/bin/bash
# Download youtube list
#
# ./dl_list.sh [ID_of_list]

#Download YouTube playlist videos in separate directory indexed by video order in a playlist
youtube-dl --add-metadata --write-info-json --embed-subs --all-subs -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=$1

