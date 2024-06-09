import logging




logging.basicConfig(level=logging.DEBUG, filename="log_ging.log", filemode="a",
format=" %(asctime)s  %(levelname)s   %(message)s ")

# format="[%(levelname)s]-%(name)s: %(message)s \n File %(pathname)s, line %(lineno)d")
# format = "%(levelname)s-%(name)s: %(message)s  File %(pathname)s, line %(lineno)d"
# format="[%(levelname)s]-%(name)s: %(message)s File %(pathname) s, line %(lineno)d")



#  регистраторы НИКОГДА не должны создаваться напрямую, а всегда через функцию уровня модуля logging.getLogger(name).
logger = logging.getLogger("X_O_R")

# logging.disable() # отключение логгера, если проставить в арг цифру уровня то будет отключ только этот уровень

# Добавлен обработчик для вывода в косоль
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)  # если поставим уровень INFO, то добавленный обработчик sh невыводит в консоль
# logger.addHandler(sh)

formatter = logging.Formatter("%(asctime)s - %(name)s -  %(levelname)s  - %(message)s " )
sh.setFormatter(formatter)
logger.addHandler(sh)

print(logger, " рутовое имя")

print(logger.handlers, "наличие обработчиков", "\n")  # наличие обработчиков



def log_test(x):
    p =  pow(x, 5)
    logger.debug(" ")
    logger.debug((p, " = p /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////", "\n"))
    return p
print(log_test(2))
