from typing import Union, Optional, Any, Final

Gitid = Union[int, float]
def anot(x: Gitid, y: int = 20) -> int:
    return (x + 1000) * y

print(anot(1000, 8), " -- >>  Union[int, float]")

def annot(x: float) -> None:
     print (f'{x}')



alias = Optional[str]
def an_not(x: float, y: alias = None) -> None:
    if y:
        print(f'{y},{x}', ' -- >> Optional[str]')
    else:
        print(f'{x}', ' -- >> Optional[str]')

an_not(22.656)

alias = Optional[str]
def ano_t(x: Any, y: alias = None) -> None:
    if y:
        print(f'{y},{x}')
    else:
        print(f'{x}')
ano_t('ANNOT')


# ress = annot(5.5)
res = anot(33.3, 10)
print(res)
print(anot.__annotations__, " <<<<<<<<<<<<<<")
print(annot.__annotations__)

cnt: int = 0
cnt = 0
cnt = 5.3

MAX_VAL: Final = 3020
MAX_VAL = 10
print(MAX_VAL)