arr=(`cat < /dev/stdin`)
arr=("${arr[@]}" "${arr[@]}" "${arr[@]}") 
echo ${arr[@]}
