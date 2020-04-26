#!/bin/bash
# wget links in file
#
# ./wget_file.sh [txtfile_with_links]

wget -c -m --no-cookies -np -r --limit-rate=2m -i $1
