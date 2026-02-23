def digit_root(num):
    while num > 9:
        num = sum(int(symb) for symb in str(num))
    return num

summ = digit_root(97569)
print(summ)