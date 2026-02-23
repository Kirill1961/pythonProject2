import math

def calculate_probability(k, p, n):
    """
    Рассчитывает вероятность успешного подбора от 0 до k включительно.
    """
    probability_sum = 0
    for i in range(k + 1):
        probability_sum += math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return probability_sum

def find_max_length_password(target_probability, p, max_attempts):
    """
    Находит максимально возможную длину пароля, чтобы гарантированно успеть открыть сейф.
    """
    k = 1  # Начинаем с длины пароля 1
    probability_sum = calculate_probability(k, p, max_attempts)

    while probability_sum < target_probability:
        k += 1
        probability_sum = calculate_probability(k, p, max_attempts)

    return k

# Условия задачи
target_probability = 0.5 # Гарантированная вероятность успеха
p = 0.7  # Вероятность успешного подбора символа
max_attempts = 30  # Максимальное время в секундах (30 минут)

# Находим максимально возможную длину пароля
max_length = find_max_length_password(target_probability, p, max_attempts)

# Вывод результата
print(f"Максимально возможная длина пароля: {max_length}")