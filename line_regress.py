import random
import matplotlib.pyplot as plt
import turtle
""" Линейная регрессия """

""" Дано axis weight /ось х   и   axis height / ось у,   данные - точки datas, 
    и  произвольная наклонная прямая с угловым quotient 0.64,
    надо вычислить смещение наклонной лини для минимизации вертикальные расстояния от линии до точек """

# используется формула пpоизводной в точке:k = ▲у / ▲х -> ▲ quotient = height / ▲ weight -> height=quotient * weight

def line_regres(intercept):
    datas = [(2.9,1.4), (2.3, 1.9), (0.5, 3.2)] #  данные с кординатами по осям
    while True:
        for data_weight in datas:
            # print(datas)
            weight = data_weight[0] # по оси Х
            height = data_weight[1] # по оси У
            # print(weight)
            predict_height = intercept + (0.64 * weight) #
            print(height, ' height ;', predict_height, ' predict_height')#если predict_height убывает то ф-я убывающая
            residuals = height - predict_height
            print(residuals, ' residuals')
            sum_square_resuduals = (residuals)**2
            print(sum_square_resuduals)
        # return
        print('')
        print(' Второй вариант расчёта сумм квадратов отклонений residuals через listcomprehension')
        print('')
        data_intercept = [0, 0.25, 0.5, 0.75, 1] # значения пересечения линии с axis height
        sum_square_resuduals = [(data_weight[1] - (intercept + (0.64 * data_weight[0])))**2
                                for intercept in data_intercept for data_weight in datas]
        print(sum_square_resuduals, ' square')
        # return sum((sum_square_resuduals))
        return  sum_square_resuduals

xs = range(15) # Создаём диапазон значений для функции square
plt.title('sum_square_resuduals')
plt.plot(xs, line_regres(intercept=0))  # residual - критерий истины
# plt.plot(xs, line_regres(intercept=0))
plt.show()
# print(line_regres(intercept=0), ' sum square')




