import math
import random
from typing import Union, Optional, Any, Final
from operator import  itemgetter

# x = [ 0.49, 0.41, 0.40, 0.25]
# y = [ 0.32, 0.37, 0.34, 0.20]
# x_data = [ 49, 41, 40, 25]
# y_data = [ 32, 37, 34, 20]
# x = [ 49, 41]
# y = [ 32, 37]
x_data = [49]
y_data = [32]
print(x_data, y_data, " значения для SGD ")

index_random_for_x_y = random.choice([index_x for index_x, index_y in enumerate(y_data)])
print(index_random_for_x_y, " random index")
data_x_y = [x_data[index_random_for_x_y], y_data[index_random_for_x_y]]
print(data_x_y, " random index  data_x_y  ")

# theta_0 = [random.random(), random.random()]
theta_0 = [0, 1]



def e_r(x, y, theta_n):
    a, b = theta_n
    # print(y - (b * x + a), " e_r residual")
    return y - (a + b * x)



def s_e(x, y, theta_n):
    # a, b = theta_n
    print(e_r(x, y, theta_n)**2, " square_e_r")
    return e_r(x, y, theta_n)**2

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


def s_e_g(data_x_y, theta_n):
    x, y = data_x_y
    print (e_r(x, y, theta_n), " e_r // residual")
    print(theta_n, " theta_n_for_s_e_g")
    return [-2 * e_r(x, y, theta_n) , -2 * x * e_r(x, y, theta_n)] # Градиент ᶐ и β


" Шаг сходимости / Step_Size"
# step_size = 1 / min(n, nm), где n - номер итерации, nm - ограничение min размера шага при больших значениях n
# step_size = 1 / min(n + 1, nm)

def minimz(data_x_y, theta_0, l_r):

    # data = zip(x, y)

    n = 0
    while n < 100:
        n += 1
        # data = zip(x, y)
        min_step = 100 # min_step ограничение шага по минимуму
        # print(theta_0, " theta_0", "\n")
        print("\t" * 3, n, "\n")
        print(data_x_y, " data_x_y")


        grad_resedual_a_b = [grad_a_b for grad_a_b in [s_e_g(data_x_y, theta_0)  ]]# Градиент Loss по ᶐ и β
        print(grad_resedual_a_b, " grad_ᶐ_β")

        sum_grad_a, sum_grad_b = [], []  # Сумма градиентов ᶐ и β сохраняем в sum_grad_a, sum_grad_b
        [( sum_grad_a.append (sum_grad_for_a), sum_grad_b.append (sum_grad_for_b))  # Сумма градиентов ᶐ и β
             for sum_grad_for_a, sum_grad_for_b in grad_resedual_a_b ]
        sum_grad_a_b = [sum(sum_grad_a), sum(sum_grad_b)] # Сумма градиентов ᶐ и β
        print(sum_grad_a_b, " sum_grad_ᶐ_β" )

        # step_size_for_a_b = [ (step_size_a_b * l_r) for step_size_a_b in sum_grad_a_b]
        # print(step_size_for_a_b, " step_size_ᶐ_β")
        # print([sum_grad_a_b[k] * step_size_for_a_b[k] for k in range(2)], " sum_grad_a_b[k] * step_size_for_a_b[k]")
        # theta_n = [theta_0[k] - sum_grad_a_b[k] * step_size_for_a_b[k] for k in range(2)]

        step_size_for_a_b = 1 /( min(n, min_step)) * l_r # шаг привязан к числу итераций, min_step ограничение шага
        print(step_size_for_a_b, " step_size_ᶐ_β")
        print(theta_0, " >>>>>>>>>>>>>theta_0")
        theta_n = [theta_0[k] - sum_grad_a_b[k] * step_size_for_a_b for k in range(2)]  # индекс k - выбор для ᶐ или β
        print(theta_0, " <<<<<<<<<<<<<theta_n")
        theta_0 = theta_n
        # print(theta_0, " theta_0 = theta_n")




        #
        # float_inf = float("-inf") or float("inf")  # Передали в переменную минус-бесконечность для условия останова
        #
        # if theta_n[0] and theta_0[1] != float_inf :
        #     minimz
        # else:
        #     return  theta_0


        # if theta_0 == theta_n:
        #     return  theta_0



print(minimz(data_x_y, theta_0, 0.01), " minimz")

    # pass



    # return theta_n

# minimz(x, y, theta_0, 0.01)