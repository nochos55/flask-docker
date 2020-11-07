#!/bin/bash
trap "exit" SIGINT
while :
do  
	echo $(date) Writing fortune to /var/htdocs/index.html  
	fortune > templates/test.html  
	sleep 10
done
