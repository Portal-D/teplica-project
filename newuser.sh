#!/bin/bash

a=`cat /mnt/raw/user`
cat /dev/null > /mnt/raw/user



mysql -u root -pkoshak << EOF
use telegram;
INSERT INTO users(chatid) VALUES('$a');
EOF
