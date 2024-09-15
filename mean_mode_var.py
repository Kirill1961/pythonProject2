import math as mt

# d = {1: 65, 2: 72, 3: 81, 4: 88, 5: 65, 6: 72, 7: 76, 8: 88, 9: 92, 10: 7}
d1 = {1: 23, 2: 27, 3: 25, 4: 30, 5: 22, 6: 28, 7: 26, 8: 29, 9: 24, 10: 31,
      11: 20, 12: 32, 13: 28, 14: 26, 15: 30, 16: 21, 17: 27, 18: 29, 19: 25,
      20: 33, 21: 22, 22: 28, 23: 24, 24: 31, 25: 26, 26: 30, 27: 23, 28: 29,
      29: 32, 31: 21, 32: 27, 33: 26, 34: 30, 35: 24, 36: 28, 37: 22, 38: 31, 39: 25, 40: 29}

# sample 30%
d = dict(list(d1.items())[0:14])

mean = sum([j for j in d.values()]) / len(d)
print(f"mean {mean}")

count = {}
for i in d.values():
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

mode = [key for key, val in count.items() if val == max(count.values())]
print(f"mode {mode}")

var = sum((i - mean) ** 2 for i in d.values()) / (len(d) - 1)
print(f"variance {var:.2f}")

sd = mt.sqrt(var)
print(f"sd {sd:.2f}")

se = sd / mt.sqrt(len(d))
print(f"se {se:.2f}")

ci_below, ci_higher = mean - se * 1.96, mean + se * 1.96
print(f"ci {ci_below:.2f}, {ci_higher:.2f}")

# Нулевая
mu = 26
z = (mean - mu) / se
print(f"z-stat {z:.2f}")