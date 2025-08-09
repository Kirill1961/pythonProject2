import torch
import torch.nn as nn
import torch.optim as optim

# Входные и целевые данные
x = torch.tensor([[0.5, 0.8]], requires_grad=True)  # входной слой
y_target = torch.tensor([[1., 0.]])  # целевое значение

# Модель: 2 входа → скрытый слой из 3 нейронов → 1 выход
model = nn.Sequential(
    nn.Linear(2, 3, bias=True),  # w_h
    nn.ReLU(),
    nn.Linear(3, 3, bias=True),
    nn.ReLU(),
    nn.Linear(3, 2),   # w_y
)


# Функция потерь и оптимизатор
loss_fn = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Шаг обучения (одно обновление)
for epoch in range(200):
    y_pred = model(x)                         # прямое распространение
    loss = loss_fn(y_pred, y_target)         # вычисление ошибки
    loss.backward()                          # обратное распространение (autograd)
    optimizer.step()                         # обновление весов
    optimizer.zero_grad()                    # обнуляем градиенты

print(y_pred)

