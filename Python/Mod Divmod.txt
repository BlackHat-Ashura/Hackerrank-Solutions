dividend = int(input())
divisor = int(input())
div_mod = divmod(dividend, divisor)
for i in div_mod:
    print(int(i))
print(div_mod)
