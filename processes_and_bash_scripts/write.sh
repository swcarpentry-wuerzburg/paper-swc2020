#!/bin/bash

# Call the test.py script with all elements in min_array

min_array=(1 2 3)
for i in "${min_array[@]}"
do
	python3 test.py $i
done

