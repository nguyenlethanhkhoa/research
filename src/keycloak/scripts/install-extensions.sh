#!/bin/bash

cd ../extensions
if [ ! -d "target" ]
then
  mkdir target
fi
cd src
for d in $(find  -maxdepth 1 -type d)
do
  if [ "$d" != "." ]
  then
    cd $d
    mvn package
    cd target
    for f in $(find -name "*.jar")
    do
      cp $f ../../../target
    done
    cd ../..
  fi
done