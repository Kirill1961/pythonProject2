


class Box:
    def __init__(self, cat=None):
        self.cat = cat  # объект , data содержащаяся в узле
        self.nextcat = None  # ссылка на след узел


class LinkedList:
    def __init__(self):
        self.head = None  # головной он же текущий узел, головной становится текущим если уже есть 1й узел

    def addToEnd(self, newcat):

        newbox = Box(newcat)  # трафарет для создания первого и последующих узлов
        if self.head is None:  # проверяем на наличие головного узла
            self.head = newbox

            return
        lastbox = self.head
        while lastbox.nextcat:  # проверяем весь список на наличие узлов по ссылке на след узел
            lastbox = lastbox.nextcat  # с последнего узла ПЕРЕХОДИМ по ссылке nextcat на newbox
            print(lastbox.cat, '   lastbox.nextcat 11111 ')
        lastbox.nextcat = newbox  # это последний узел, он вне цикла
        print(lastbox.cat, '   lastbox.nextcat 2222')

    def get(self, catIndex):
        lastbox = self.head
        boxIndex = 0
        while boxIndex <= catIndex:
            if boxIndex == catIndex:
                return lastbox.cat
            boxIndex = boxIndex + 1
            lastbox = lastbox.nextcat


    def contains(self, cat):
        lastbox = self.head

        while lastbox is not None:  # прокручиваем через while - lastbox в котором данные из экземпляра
            if cat == lastbox.cat:  # если запрошенное значение cat находится в цепочке узлов lastbox.cat то True
                print('This node found :', cat, end=' ')  # вывод присутствующего узла
                return True
            else:

                lastbox = lastbox.nextcat  # если нет, запрошенного значения в данном связанном списке, то lastbox
        print('This node definded : ', cat,
              end=' ')  # вывод отсутствующего узла, в цикле выводить нельзя тк будут повторения
        return False  # инициализируем с сcылками на узлы nextcat, где последний nextcat = None


    def __str__(self):  # Используем ф-цию __str__ для вывода в строчном формате

        lastbox = self.head
        line = '['
        while lastbox.nextcat:  # Прокручиваем все боксы lastbox по ссылкам nextcat -> while lastbox.nextcat:
            # line = '[['   # Назначили строчную переменную куда будут помещаться str данные cat
            # line += '+ = '   # Если ниже поставить знаки + =, то получим конкатенацию str значений
            line += lastbox.cat + ','   # прибавляет узлы lastbox.cat из итерации while lastbox.nextcat:
            # line += ','
            lastbox = lastbox.nextcat
        line += lastbox.cat + ']'

        return line

    # def __str__(self):  # Используем ф-цию __str__ для вывода в строчном формате
    #
    #     lastbox = self.head
    #     line = '['
    #     while lastbox.nextcat: # Прокручиваем все боксы lastbox по ссылкам nextcat -> while lastbox.nextcat:
    #         # line = '['   # Назначили строчную переменную куда будут помещаться str данные cat
    #         # line += '+ = '   # Если ниже поставить знаки + =, то получим конкатенацию str значений
    #         line +=  lastbox.cat  + ',' # прибавляет узлы lastbox.cat из итерации while lastbox.nextcat:
    #         # line += ','
    #         lastbox = lastbox.nextcat
    #     line += lastbox.cat + ']'
    #
    #     return line
    def LLprint(self):
        currentCat = self.head
        print("LINKED LIST")
        print("-----")
        i = 0
        while currentCat is not None:
            print(str(i) + ": " + str(currentCat.cat))
            i += 1
            currentCat = currentCat.nextcat
        print("-----")

    """ _________________Мои варианты прокрутки узлов с содержимым_________________
    1й вариант с условием по пустому списку, цикл перебирает узлы без точечной нотации /while lastcat :/, 
    а  return прерывает цикл и возвращает значение """

    # def get_cat(self):
    #     lastcat = self.head
    #     l = [lastcat.cat]
    #     while lastcat :
    #         lastcat = lastcat.nextcat
    #         if lastcat is not None:
    #             l.append(lastcat.cat)
    #         else: return l

    """ 2й вариант без условия по empty списку, но цикл перебирает не узлы lastcat,
         а ссылки на узлы /while lastcat.nextcat/ """

    def get_cat(self):
        lastcat = self.head
        l = [lastcat.cat]
        while lastcat.nextcat:
            lastcat = lastcat.nextcat
            l.append(lastcat.cat)
        return l

    """ 3й вариант без условия по empty списку, но цикл перебирает ссылки на узлы /while lastcat.nextcat/,
        а имена узлов мы сохраняем в переменную node вытаскивая по ссылке из текущего узла/node += lastcat.cat/"""

    # def get_cat(self):
    #     lastcat = self.head
    #     node = ' '
    #     while lastcat.nextcat:
    #         node += lastcat.cat + ','
    #         lastcat = lastcat.nextcat
    #     node += lastcat.cat
    #     return node
    """ ____________________Мой вариант поиска по индексу________________"""
    # def get_from_index(self, index):
    #     get_node = self.head
    #     index_node = 0
    #     while get_node.nextcat:
    #         if index == 0:
    #             return get_node.cat
    #         index_node += 1
    #         get_node = get_node.nextcat
    #         if index_node == index:
    #             return get_node.cat
    """ ____________________Вариант по индексу от  LEETCODE_________________________ """
    def get_from_index(self, index):
        get_node = self.head
        index_node = 0
        while  index_node <= index : # цикл крутит пока index_node < или = заданному index
            if index_node == index: # как только index_node и index сравнялись возвращается значение из linkedlist
                return get_node.cat  #  возврат значения из linkedlist
            index_node += 1
            if index > index_node:   # фильтр на случай несуществующего индекса
                return 'This index not found' # выводим сообщение
            else:
                get_node = get_node.nextcat


# cib = Box('Lis')
# print((cib.__dict__), '(((')
# print(cib.cat, cib.nextcat, ' next')
# cnb = LinkedList()
cwb = LinkedList()

cwb.addToEnd('100')
cwb.addToEnd('250')
cwb.addToEnd('350')
cwb.addToEnd('450')
# print(cwb.get_cat())
print(cwb.get_from_index(5), '    cwb.get_from_index(5) ')
print(cwb.get(0), '   cwb.get(0)  ')

# cnb = LinkedList()
# cnb.addToEnd('400')
# cnb.addToEnd('200')
# cnb.addToEnd('300')
# cnb.addToEnd('500')


# print(cnb, 'cnb  ')
print(cwb, 'cwb')
# print(cwb.__dict__, '__dict____dict____dict__')
# print(cwb.contains('350'), 'cwb.contains')

# print(cwb, 'cwb cwb cwb ')
# print(cwb.LLprint())
# print(LinkedList.LLprint(cnb))
# print('\t '*6, cnb.__dict__, 'cnb head')
# print('\t '*6,cnb.get(2), '- output get by index cnb')
# print('\t '*6,cwb.get(0), '- output get by index cwb')


# print('\t '*8,LinkedList.contains(cnb, 'Lis contains'))
# print(LinkedList.addToEnd(cnb, 'Lis'))

# print(LinkedList.contains(cnb, 'Mur'))
# print(cnb.contains('500'), 'cnb.contains')
# print(LinkedList.addToEnd.__class__, '//////')


# задаём список списков -> трансформируем в связанный -> сортируем -> и выводим связ список
list = [[1, 4, 3], [2, 5,  11], [3, 7, 6, 24, 0]]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __call__(self, g="Kirill", *args, **kwargs):
        print('Hellow', g)

    def mergeKLists(self, lists,*args, **kwargs):

        stlist = []
        index = 0
        while index < len(list):
            index += 1
            next = ListNode(list[index - 1])
            if lists is None:
                lists = next
            nextlists = next
            # print(nextlists.val,nextlists, '      Связали исходный список списков list')
            while nextlists.val :
                nextval = ListNode(nextlists.val.pop(0))
                print('\t'*2,nextval.val,'  ->  Изъяли из связанных списков отдельные значения ;     ',  nextval, '   и'
                                             ' связали эти значения ')
                stlist.insert(0, nextval.val)
        linkedsort = sorted(stlist)
        print(linkedsort)


obj1 = Solution()
obj1.mergeKLists(list)
obj1()  # для вызова __call__
