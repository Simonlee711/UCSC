#!/bin/bash

#disk usage size script

cd /Users/simonlee/leesimon-am129-fall21 
du | sort -n -r | head -3 > dirSize.txt
mv dirSize.txt /Users/simonlee/leesimon-am129-fall21/Homework/hw1/code

