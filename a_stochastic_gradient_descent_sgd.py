
import random



def square(x_x, y_y, t):
    # print(x, y, t, ' square')
    return (y_y - t * x_x)**2  # Loss function целевая функция - квадратичное отклонение  / Loss function

def derivative(x_x, y_y, t):    # производная целевой ф-ции Loss function по theta - (y_y - (t * x_x))**2
    return -2 * x_x * (y_y - t * x_x)   # " t " - это theta - регрессионный коэфф, угол наклона




v = [random.randint(-10, 10) for i in range(2)] # рандом генератор для theta, х, у
v_theta = random.choice(v)
v_theta_for_sgd = 0.1 * v_theta if v_theta > 0 else v_theta * -1 # вектор параметров theta, * -1 это если random отриц.
x_for_sgd = [0.1 * i_x for i_x in v]     # из генератора v берём Х
y_for_sgd = [i_y ** 2 for i_y in x_for_sgd] # из У = Х**2
print(v, v_theta, ' theta_0')
toleerance = 0.00001  # константа точности расчёта



# print(different_guotient(square, v[0], h=0.0001), ' different_guotien')
# print(sum_of_squares_gradient(v), ' sum_of_squares_gradient')


def in_random_order(data):
    indexes = [i for i,_ in enumerate(data)]
    # print(indexes, ' indexes')
    random.shuffle(indexes)  # перемешивание индексов данных для случайного выбора
    for i in indexes:
        print(i, data[i], '  <-> i, data[i]')
        yield data[i]
        # return data
# for y in random_order([11,22,33]):
#     print(y)



def scalar_multiplay(step_alfa, gradient_i_for_next_theta):
    print('\t'*16, step_alfa * gradient_i_for_next_theta, ' scalar_multiplay')
    return step_alfa * gradient_i_for_next_theta


def vector_subtract(theta_old, gradient_for_theta):
    print('\t' * 16, theta_old - gradient_for_theta, ' theta - scalar_multiplay')
    return theta_old - gradient_for_theta


def minimize_stohastic(target_fn, gradient_fn, x, y,  theta_0, alfa_0 = 0.01):

    data = list(zip(x, y))
    print(data, ' data = list(zip(x, y))')
    theta = theta_0  # theta -  это theta - оценочный коэфф
    alfa = alfa_0
    min_theta, min_value = None, float('inf') # определяем минимальные значения theta и value
    iterration_whith_no_improvement = 0
    iterration_whith_no_improvement_condition_for_value = 0
    while iterration_whith_no_improvement < 100 and iterration_whith_no_improvement_condition_for_value < 500:
        value = sum (target_fn(x_i, y_i, theta) for x_i, y_i in data)# Сумма квадратов residual (square)
        if value < min_value:          # условие если значение лежит на прямой те апроксимирована к прямой
            min_theta, min_value = theta, value
            print(' ')
            iterration_whith_no_improvement = 0
            iterration_whith_no_improvement_condition_for_value += 1
            print('\t' * 6, '*',iterration_whith_no_improvement_condition_for_value, '*' )
            print(' ')
            alfa = alfa_0
        else:
            iterration_whith_no_improvement += 1
            print('\t' * 6, '<<',iterration_whith_no_improvement, '>>')
            alfa *= 0.9  # Стартовый оценочный коэфф (slope)
            # TODO  batch - случайным образом выбираем пару Х и У
            for x_i, y_i in in_random_order(data):
                print('\t'*10, alfa, ' alfa ')
                print('\t' * 2, value, ' value  <-->', min_value, ' min_value ')
                gradient_i = gradient_fn(x_i, y_i, theta) # градиент Loss(target_fn) по  theta i-ое
                print(gradient_i, ' gradient_i')
                print('\t' * 16, theta, ' theta_previous ')
                theta = vector_subtract(theta, scalar_multiplay(alfa, gradient_i))# вычисление следующ. theta
                print('\t'*16,  theta, ' theta ;', min_theta, ' min_theta >>')
                print(' ')
    return min_theta # минимальное значение точки на графике -0.26141959552258875

print(minimize_stohastic(square, derivative, x_for_sgd,  y_for_sgd , v_theta_for_sgd , alfa_0 = 0.01), ' minimize_stohastic')


