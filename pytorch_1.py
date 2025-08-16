import torch
import torch.nn as nn
import torch.optim as optim

# Входные и целевые данные

# TODO requires_grad=True - но поддержка авто-дифференцирования для входа не нужна,
#  в backward вход не участвует и зря запоминаются вычисления
x = torch.tensor([[0.5, 0.8]], requires_grad=True)  # входной слой
y_target = torch.tensor([[1., 0.]])  # целевое значение

# Модель: 2 входа → скрытый слой из 3 нейронов → 1 выход
model = nn.Sequential(
    nn.Linear(2, 3, bias=True),  # w_h_1
    nn.ReLU(),
    nn.Linear(3, 3, bias=True),  # w_h_2pos_label
    nn.ReLU(),
    nn.Linear(3, 2),   # w_y
)

# TODO model.parameters() - только обучаемые параметры из модели для оптимизатора,
#  * layers - слои
#  * bias - смещение
for param in model.parameters():
    print(type(param), param.size())

# Функция потерь и оптимизатор
loss_fn = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)



# Шаг обучения (одно обновление)
for epoch in range(200):
    y_pred = model(x)                         # прямое распространение
    loss = loss_fn(y_pred, y_target)         # вычисление ошибки
    loss.backward()                          # обратное распространение (autograd)
    optimizer.step()                         # обновление весов
    optimizer.zero_grad()                    # обнуляем градиенты

print(y_pred)

