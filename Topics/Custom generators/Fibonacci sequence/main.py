def fibonacci(n):
    values = []
    for i in range(0, n):
        if i == 0 or i == 1:
            values.append(i)
        else:
            values.append(values[i - 1] + values[i - 2])
        yield values[-1]
