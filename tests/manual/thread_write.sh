#!/bin/bash

for i in 1 2 3 4 5;
do
		sleep 1;
		echo main $i;
		echo $(echo thread $i);
done;