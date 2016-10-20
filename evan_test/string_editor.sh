#!/bin/bash

p = $my_file

while read p; do 
    if [[$p == *".css"* ]]; then
        sed -i -- 's/href="/href="\/static\//' $p

    if [[$p == *".html"* ]]; then
        sed -i -- 's/href="/href="\//' $p
done
