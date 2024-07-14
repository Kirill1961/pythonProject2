import logging

def s4l(phr: str, let: str) -> set:
    return set(let).intersection((set(phr)))


print(s4l("assddffgg", 'gf'), "\n")



import requests
# logging.basicConfig(level="DEBUG", filename="asa45.log")

logging.basicConfig(level=logging.DEBUG, filename="imp2.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")



logger = logging.getLogger("Kirill") # задаём root name для рутового логгера

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)  # если поставим уровень INFO, то добавленный обработчик sh невыводит в консоль
logger.addHandler(sh)

print(logger, "логгер", "\n")

logger.setLevel("DEBUG") # задаём уровень логгера

print(logger.level,"уровень логгера", "\n") # уровень логгера

print(logger.handlers, "наличие обработчиков",  "\n") # наличие обработчиков

# print(dir(logger))


def main(name):
    logger.debug(f" Enter in the main() function: name = {name}")
    value = name + " Good programmer"
    logger.debug(value)
if __name__==  "__main__":
    main(" Kirill")

#
# x = 3
# y = 4
#
# logging.info(f"The values of x and y are {x} and {y}.")
# try:
#     x/y
#     logging.info(f"x/y successful with result: {x/y}.")
# except ZeroDivisionError as err:
#     logging.error("ZeroDivisionError",exc_info=True)
