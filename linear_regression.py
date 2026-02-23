def predict(alfa, beta, x_i):
    return x_i * beta + alfa


def error(
    alfa,
    beta,
    x_i,
    y_i,
):
    residual = y_i - predict(alfa, beta, x_i)
    print(residual)
    return residual


x = [2, 4, 6]
y = [20, 40, 60]


def sum_of_square_error(*residual):
    return sum(
        [
            error(
                *residual,
                x_i,
                y_i,
            )
            ** 2
            for x_i, y_i in zip(x, y)
        ]
    )


print(sum_of_square_error(5, 0.5))
