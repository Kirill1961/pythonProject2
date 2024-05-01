import numpy as np
import logging


logging.basicConfig(level=logging.DEBUG, filename="x_o_r.log", filemode="w")
logger = logging.getLogger("X_O_R")
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)


# logger.debug(epoch)
def f(x):
    return 2 / (1 + np.exp(-x)) - 1  # гиперболический тангенс


def df(x):
    return 0.5 * (1 + x) * (1 - x)


W1 = np.array(([[-0.2, 0.3, -0.4], [0.1, -0.3, -0.4]])) # w скрытого
W2 = np.array([0.2, 0.3])  # w выходного
logger.debug(W1[0, :])


def go_forward(inp):
    sum = np.dot(W1, inp)  # вход скрытый
    out = np.array([df(x) for x in sum])  # выход скрытого
    # logger.debug((out, "out"))

    # logger.debug((sum, "sum 1"))
    sum = np.dot(W2, out)  # вход выходной
    y = f(sum)  # выход выходного

    # logger.debug((y, out))
    return y, out
# [go_forward(x[0:3]) for x in epoch]


def train(epoch):

    global W2, W1
    lmd = 0.0001
    N = 5
    count = len(epoch)

    for _ in range(N):

        x = epoch[np.random.randint(0, count)]
        # logger.debug((x[-1], " delta"))
        y, out = go_forward(x[0:3])  # на старте взяли выходы скрытого и выходного из прямого распространения
        # logger.debug((out, "out"))
        e = y - x[-1]  #  ошибка
        delta = e * df(y)

        W2[0] = W2[0] - delta * out[0] * lmd
        W2[1] = W2[1] - delta * out[1] * lmd
        logger.debug((W2[1], " W2, f(out)"))
        delta2 = f(out) * delta * W2
        logger.debug((W1[0, :], " W1"))
        W1[0, :] = W1[0, :] - delta2[0] * np.array(x[0:3]) * lmd
        W1[1, :] = W1[1, :] - delta2[1] * np.array(x[0:3]) * lmd


epoch = [(-1, -1, -1, -1),
         (-1, -1, 1, 1),
         (-1, 1, -1, -1),
         (-1, 1, 1, 1),
         (1, -1, -1, -1),
         (1, -1, 1, 1),
         (1, 1, -1, -1),
         (1, 1, 1, -1)]

train(epoch)
for x in epoch:
    y, out = go_forward(x[0:3])
    logger.debug(f"{y} => {x[-1]}")
    # print(f"{y} =  > {x[-1]}")