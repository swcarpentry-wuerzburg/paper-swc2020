#!/bin/bash

# Copy the all files from the folder and ending in .file to the current
# directory and rename them to be folder_NAME

for i in folder/*.file
do
    j=${i##*/}
    cp $i folder_$j
done
