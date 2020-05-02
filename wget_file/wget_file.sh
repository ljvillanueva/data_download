#!/bin/bash
# wget links in file
#
# ./wget_file.sh [where_to_save] [txtfile_with_links]

wget -c -m --no-cookies --random-wait -np -r --limit-rate=2m -P $1 -i $2
