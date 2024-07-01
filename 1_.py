a = [0.98, 0.14, 0.44, 0.13, 0.09, 0.19, 0.53, 0.7]


def ou(x):

    def ine(y):
        return x * y

    return ine(5)


print(ou(2), "ok")

g = (["q", "w", "e", "r"], ["q", "w", "e", "r"], ["q", "w", "e", "r"])

with open("names.csv", "r") as n:
    while True:
        n_ = n.readline()
        print(n_)
        if not n_:
            break

k = 10
print(f"{k}")
