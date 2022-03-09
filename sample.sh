#! /bin/bash

user='Abhinav'

if [ $user = 'CUSAT' ]
then
	echo 'Hello CUSAT'
else
	echo "Hello $user"
fi

i=0

while [ $i -lt 5 ]
do
	echo $i
	i=`expr $i + 1`
done

