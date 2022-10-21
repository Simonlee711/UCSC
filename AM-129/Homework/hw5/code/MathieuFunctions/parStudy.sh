#!/bin/bash

# Call the mathieu executable for a variety of q-values

res=201

for q in {0..40}
do
    printf -v Q "%02d" $q
    sed "s/RES/$res/g" mathieu.init.ref | sed "s/QQ/$Q/g" | sed "s/QVAL/$q/g" > mathieu.init
    ./mathieu.ex
done
