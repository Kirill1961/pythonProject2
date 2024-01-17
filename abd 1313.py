import math
import random
from typing import Union, Optional, Any, Final
from operator import itemgetter

# x = [ 0.49, 0.41, 0.40, 0.25]
# y = [ 0.32, 0.37, 0.34, 0.20]
x = [ 49, 41, 40, 25]
y = [ 32, 37, 34, 20]
# x = [ 49, 41]
# y = [ 32, 37]
# x = [49]
# y = [32]
print(x, y)
theta_0 = [0, 1] # В ГЕНЕРАТОРЕ оценочных коэфф, alpha, beta ставим под индексы в соответствии с местами в функциях
               # , a = 0 (intersept), b = 1 (slope)
#
# theta_0 = [random.random(), random.random()]
print(theta_0, " a_b_theta_0")


def e_r(x, y, theta_n):
    a, b = theta_n
    # print(y - (b * x + a), " e_r residual")
    return y - (a + b * x)



def s_e(_x, _y, theta_n):
    # a, b = theta_n
    print(e_r(_x, _y, theta_n) ** 2, " square_e_r")
    return e_r(_x, _y, theta_n) ** 2

# Сумма квадратов отклонений
# def sum_s_e(x, y, theta_n):
#     data= zip(x, y)
#     # print([s_e(x, y, theta_n) for x, y in data])
#     return sum(s_e(x, y, theta_n) for x, y in data)
# print(sum_s_e(x, y, theta_0))


# def e_r(x, y, theta_n):
#     a, b = theta_n
#     print(y - (b * x + a), " e_r residual")
#     return (y - (b * x + a))


def s_e_g(x_, y_, theta_n):
    print (e_r(x_, y_, theta_n), " e_r // residual")
    print(theta_n, " theta_n_for_s_e_g")
    return [-2 * e_r(x_, y_, theta_n) , -2 * x_ * e_r(x_, y_, theta_n)] # Градиент ᶐ и β


" Шаг сходимости / Step_Size"
# step_size = 1 / min(n, nm), где n - номер итерации, nm - ограничение min размера шага при больших значениях n
# step_size = 1 / min(n + 1, nm)

def minimz(x, y, theta_0, l_r):

    # data = zip(x, y)
    n = 0
    while n < 100:
        n += 1
        data = zip(x, y)
        nm = 110
        print(theta_0, " theta_0", "\n")
        print("\t" * 3, n, "\n")
        # theta_n = [theta_0[k] - s_e_g(x, y, theta_0)[k] for x, y in data for k in range(2)]
        # print(theta_n, " theta_n")

        grad_resedual_a_b = [grad_a_b for grad_a_b in [s_e_g(x, y, theta_0) for x, y in data]]# Градиент Loss по ᶐ и β
        print(grad_resedual_a_b, " grad_ᶐ_β")

        sum_grad_a, sum_grad_b = [], []
        [( sum_grad_a.append (sum_grad_for_a), sum_grad_b.append (sum_grad_for_b))
             for sum_grad_for_a, sum_grad_for_b in grad_resedual_a_b ]
        sum_grad_a_b = [sum(sum_grad_a), sum(sum_grad_b)]
        print(sum_grad_a_b, " sum_grad_ᶐ_β" )

        # step_size_for_a_b = [ (step_size_a_b * l_r) for step_size_a_b in sum_grad_a_b]
        # print(step_size_for_a_b, " step_size_ᶐ_β")
        # print([sum_grad_a_b[k] * step_size_for_a_b[k] for k in range(2)], " sum_grad_a_b[k] * step_size_for_a_b[k]")
        # theta_n = [theta_0[k] - sum_grad_a_b[k] * step_size_for_a_b[k] for k in range(2)]

        step_size_for_a_b = 1 /( min(n, nm)) * l_r
        # step_size_for_a_b = 1 / n if n > l_r else l_r
        print(step_size_for_a_b, " step_size_ᶐ_β")
        theta_n = [theta_0[k] - sum_grad_a_b[k] * step_size_for_a_b for k in range(2)]

        print(theta_n, " theta_n")
        theta_0 = theta_n
        print(theta_0, " theta_0 = theta_n")
        float_inf = float("-inf") # Передали в переменную минус-бесконечность для условия останова
        # if step_size_for_a_b[0] or step_size_for_a_b[1] > 0.001  :
        #     minimz
        if theta_n[0] and theta_0[1] != float_inf :
            minimz
        else:
            return  theta_0
        # sum_grad_a_b = sum(grad_resedual_a_b)
        # print(sum_grad_a_b  , " sum(grad_resedual_a_b)")
        # step_size_a_b = sum_grad_a_b * l_r
        # theta_n = [theta_0[k] - grad_resedual_a_b[k] * step_size_a_b for k in range(2)]


        # step_size_a_b = [step_size_a_b * l_r for step_size_a_b in grad_a_b ]
        # print(step_size_a_b[0], " step_size_a")
        # print(step_size_a_b[1], " step_size_b")
        # step_size_a, step_size_b = step_size_a_b[0], step_size_a_b[1]
        # theta_n = [theta_0[k] - grad_a_b[k] * step_size_a_b[k] for k in range(2)]


        # theta_0 = theta_n
        # print(theta_0, " theta_0 = theta_n")
        # if step_size_a_b > 0.001:
        #     minimz
        # else:
        #     return  theta_0

        #     theta_n = [theta_0[k] - s_e_g(x_i, y_i, theta_0)[k] * step_size_a_b[k] for x_i, y_i in data for k in range(2)]
        #     print(theta_n, " theta_n")
        #     # theta_0 = theta_n
        #     print(theta_n, " theta_n")
        # else:
        #     print(step_size_a_b, " return")



print(minimz(x, y, theta_0, 0.01), " minimz")

    # pass



    # return theta_n

# minimz(x, y, theta_0, 0.01)