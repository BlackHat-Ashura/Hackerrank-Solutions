uniq -ci < /dev/stdin | awk '{for(i=1;i<=NF;i++) printf $i" "; print ""}'
