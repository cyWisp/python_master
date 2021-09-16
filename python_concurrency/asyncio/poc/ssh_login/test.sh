#!/bin/bash

cat "./hosts" | while read line
do
	printf "%s" ${line}
done
