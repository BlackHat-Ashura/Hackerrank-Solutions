read n

sum=0

for i in $(seq 1 $n)
do
read num
sum=$(( $sum+$num ))
done

avg=`echo "scale=4; $sum/$n "|bc`

printf "%.3f" $avg
