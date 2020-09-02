#!/bin/bash
# Download youtube video
#
# ./dl_video.sh [full_URL]

#Download YT playlist videos in separate directory indexed by video order in a playlist
youtube-dl --add-metadata --write-info-json --embed-subs --all-subs --convert-subs srt --merge-output-format "mkv" --sub-format "srt" $1

