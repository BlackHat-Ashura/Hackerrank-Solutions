while read input
do
echo "$input" | cut -f1-3
done


######################################

while read input
do
echo "$input" | cut -d $'\t' -f1-3
done
