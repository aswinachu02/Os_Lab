#! /bin/bash

echo Program by Abhinav Rajesh 20219003

read -p "Enter the value of n:" N
FACTORIAL=1

while [ $N != 0 ]
do
	
	FACTORIAL=$((FACTORIAL * N))
	N=`expr $N - 1`
done

echo "Factorial: $FACTORIAL" 

