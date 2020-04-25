wget --save-cookies cookies.txt \
     --keep-session-cookies \
     --post-data "action=login&page=&cart=&record_id=9853&
     		#Update and collapse fields
     		email=[user]%40[domain.com]
     		&password=[pass]
     		&remember_me=on" \
     --delete-after \
     --header "Origin: https://www.nap.edu" \
     --header "Referer: https://www.nap.edu/login.php?record_id=9853" \
     https://www.nap.edu/login.php?record_id=9853

