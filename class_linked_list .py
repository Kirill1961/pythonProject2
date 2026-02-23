""" В данном случае всё привязано к значению аргумента ЭКЗ связанного списка, это значение ЭКЗ подставляется
    во все переменные методов и этому значению присваивается адрес ячейки являющимся ссылкой на узел где расположится 
    данное значение.
    ЭКЗЕМПЛЯР помещается в self, поэтому переменные из ЭКЗЕМПЛЯРА (cat, nextcat,head) можно вытаскивать из self ТОЧКОЙ:
    self.cat ; self.nextcat ; self.head
    nextcat - это по факту адрес ячейки нового значения аргумента переданного из экземпляра cnb.addToEnd('400') 
    класса LinkedList, при создании нового узла newbox класса Вох. Когда класс  Вох получает значение в аргумент, 
    он присваивет этому значению адрес ячейки которая помещается в self и которая является адресом нового node.
      ____________________ ССЫЛКА - ЭТО АДРЕС ЯЧЕЙКИ_______________________________________
    В данном примере создаём два односвязанных списка - это ЭКЗ cnb и cwb"""

""" Класс Вох - служит для заполнения данными /cat/ и ссылкой /self.nextcat/ нового узла"""


class Box:
    def __init__(self, cat=None):
        self.cat = cat  # объект , data содержащаяся в узле
        self.nextcat = None  # ссылка на след узел


""" ______________Создадим класс LinkedList ______________ 
  служит для управления связанным списком: вставка node, удаление node и тд, 
  через переменную self.head передаётся ссылка на текущий node"""


class LinkedList:
    def __init__(self):
        self.head = None  # головной, текущий узел

    """ ____________________Проверим содержание NODE_____________________ 
        сколько ОБ cat находится в данном node
        locals() и globals() - вывод всех локальных и глобальных переменных"""

    def contains(self, cat):
        lastbox = self.head  # lastbox в данной инициализации является всей цепочкой значений и ссылок,
        # здесь мы из ЭКЗ, он же связ список, находящегося в self,берём переменную head(self.head),
        # в которой находятся данные и ссылки рассматриваемого ЭКЗ, создаём переменную lastbox котор ссылается на
        # self.head
        while lastbox is not None:  # прокручиваем через while - lastbox в котором данные из экземпляра
            if cat == lastbox.cat:  # если запрошенное значение cat находится в цепочке узлов lastbox.cat то True
                print('This node found :', cat, end=' ')  # вывод присутствующего узла
                return True
            else:

                lastbox = lastbox.nextcat  # если нет, запрошенного значения в данном связанном списке, то lastbox
        print('This node definded : ', cat,
              end=' ')  # вывод отсутствующего узла, в цикле выводить нельзя тк будут повторения
        return False  # инициализируем с сcылками на узлы nextcat, где последний nextcat = None

    """ _________________Добавить узел в lenkedlist___________________
        Код для вставки нового узла состоит из 2х частей:
        1 - на случай если нет 1-го узла, 
        проверяем на наличие 1-го узла если его нет , то создаём новый узел:
        newbox = Box(newcat) ->>> if self.head is None: ->>> self.head = newbox
        2. - на случай если есть кокой то узел, 
        тогда создаём след узел - lastbox(текущий узел), lastbox ссылается на self.head ->>> lastbox = self.head,
        те lastbox берёт из self.head адрес ячейки куда поместили новый date,затем прокручиваем весь lenkedlist"""

    """ Когда мы вызываем метод addToEnd для экземпляра cnb, то метод addToEnd обращается к классу  Вох
        для заполнения нового узла данными через создание экземпляра newbox . 
        Аргумент экземпляра cnb сначала подставляется арг метода addToEnd - newcat,
        а затем подставляется в классе  Вох в арг cat, класс Вох присваивает адрес ячейки для арг cat,
        этот адрес помещается в self и становится ссылкой на новый node. 
        Таким образом получаем date и ссылку на ячейку узла  
        self.cat = cat- объект , data содержащаяся в узле; self.nextcat  - ссылка на след узел"""

    def addToEnd(self, newcat):
        """ Создаём новую коробку с data newcat, newbox это экземпляр класса Вох с аргументом cat и
         ссылкой nextcat"""
        newbox = Box(newcat)  # трафарет для создания первого и последующих узлов
        if self.head is None:  # проверяем на наличие головного узла
            self.head = newbox  # если 1го узла нет, тогда newbox, становится первым узлом и все значения помещёные в newbox
            # передаются в self.head, 1й узел принимает имя переменной head.
            return
        lastbox = self.head  # текущий, следующий узел lastbox приравняв к self.head получает адрес и data через self.head
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
