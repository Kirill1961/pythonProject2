def f():
    for i in range(5):
        print('I M P O R T')
f()

def foo(x, y):
    y_sq = y[x]**2
    print(y_sq)
    return foo(x + 1, y), y_sq if x < len(y)-1 else 0
(foo(0, [10, 20, 30]))