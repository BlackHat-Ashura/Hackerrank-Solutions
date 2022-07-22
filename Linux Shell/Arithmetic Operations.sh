read EXPRESSION

printf "%.3f" `echo "scale=4; $EXPRESSION" | bc`
