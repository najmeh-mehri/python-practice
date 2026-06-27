def SumAll(*arg):
    sum = 0
    for item in arg:
        sum = sum + int(item)
    return sum
print(SumAll(2,5,6,7,4))