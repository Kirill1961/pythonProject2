from loguru import logger

# Ротирование логов + запись в формате JSON serialize=True

# logger.add("my_log.log", format="{time} {level} {message}", level="INFO", rotation="10 KB", compression="zip",
#            serialize=True)

# for _ in range(1000):
#     logger.info("INFO INFO")



logger.add("log_uru.log", format="{time} {level} {message}", level="INFO")
logger.info("OK OK")
logger.debug("NO")

#  Декоратор, ловим исключения

def d(a, b):
    return a / b

@logger.catch()
def m():
    d(1, 0)
m()

