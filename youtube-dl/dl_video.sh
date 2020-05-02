#!/bin/bash
# Download youtube video
#
# ./dl_video.sh [full_URL]

#Download YouTube playlist videos in separate directory indexed by video order in a playlist
youtube-dl --add-metadata --write-info-json --embed-subs --all-subs $1

