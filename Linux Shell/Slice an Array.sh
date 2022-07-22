arr=(`cat < /dev/stdin`)
echo ${arr[@]:3:5}
