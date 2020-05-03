#!/bin/bash
# Download youtube list
#
# ./dl_list.sh [ID_of_list]

#Download YouTube playlist videos in separate directory indexed by video order in a playlist
youtube-dl --add-metadata --write-info-json --embed-subs --all-subs --sub-format "srt" --convert-subs srt --merge-output-format "mkv" -o '$1/%(playlist)s/%(upload_date)s - %(title)s.%(ext)s' https://www.youtube.com/playlist?list=$2

