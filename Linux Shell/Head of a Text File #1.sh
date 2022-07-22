while read line
do
echo $line >> file
done
head -20 file


################################################################

head -20 </dev/stdin
