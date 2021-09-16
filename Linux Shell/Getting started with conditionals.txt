#!/bin/bash

read option

if [[ $option == 'y' || $option == 'Y' ]]
then
echo "YES"
else
echo "NO"
fi