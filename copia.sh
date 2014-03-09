#!/usr/bin/env bash

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for photo in $(find /media/ -type f);
do
  timepath=$(exiv2 -v $photo | grep timestamp | awk '{print $4}' | sed 's/:/-/g')
  year=$(echo $timepath | awk -F "-" '{print $1}')
  pdir=$(find ~/grafica/foto/$year/ -type d -name "${timepath}*")
  if [[ -z "$pdir" ]]; then
    pdir=~/grafica/foto/$year/$timepath
    mkdir $pdir
  fi
  photo_short=${photo##*/}
  if [[ ! -e "$pdir/$photo_short" ]]; then
    echo "copying $photo_short to directory $pdir"
    cp $photo $pdir
  fi
done

IFS=$SAVEIFS

