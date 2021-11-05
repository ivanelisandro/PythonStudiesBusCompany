synthetic_min = 2
synthetic_max = 3

value = float(input())

if value < synthetic_min:
    print('Analytic')
elif value > synthetic_max:
    print('Polysynthetic')
else:
    print('Synthetic')
