import re
from datetime import date, datetime


m = """January — Jan.
February — Feb.
March — Mar.
April — Apr.
May — May
June — June
July — July
August — Aug.
September — Sept.
October — Oct.
November — Nov.
December — Dec."""

d = """Monday — Mon. — Mo.
Tuesday — Tue. — Tu.
Wednesday — Wed. — We.
Thursday — Thu. — Th.
Friday — Fri. — Fr.
Saturday — Sat. — Sa.
Sunday — Sun. — Su."""

r = "\s[a-zA-Z]{3}\s"

r1 = "(\s[a-zA-Z]{3}\s)|(\b[a-zA-Z]{3})"

r2 = "(\b[a-zA-Z]{3})|(\d{2,4})"

r3 = "(\b[a-zA-Z]{3}|\d{2}(\d{2})?\b)"

r5 = "\b[a-zA-Z]{3}.\s*\d{2}(\d{2})?"

r_abc_2_4 = r"[a-zA-Z]{3}\d{2}(\d{2})|[a-zA-Z]{3}\d{2}"

r_abc_2_4_1 = "[\w+]{3}\d{2,4}"

r_month_separ = r"([A-Z]\w{2}[a-zA-z]?\d{2,4})"

r_day_month_year_dayweek_my = r"(?:[A-Z]\w{2}[a-zA-z]?\d{2}[A-Z]\w{2}[a-zA-z]?\d{4})"

r_day_month_year_dayweek_gpt = r"[A-Z][a-zA-Z]{2}\d{2}[A-Z][a-zA-Z]{2,3}\d{2}(?:\d{2})?"

r_day_month_year = r"\d{2}[A-Z][a-zA-Z]{2,4}\d{2}(?:\d{2})?"

rgpt = r'\b[a-zA-Z]{3}\d{2}(\d{2})?\b'

rgpt2 = r'\b\w{3}\d{2,4}\b'
"""
Subject: Plans for cable
Date: Mon, 26 Aug 2002 16:26:01 -1700
Delivered-To: zzzz@localhost.example.com"""

# text ="""
# SubjectPla5478nsforcable
# DateMon26Aug2002162601Truk1700
# Delivered-Tozzz22z@localhostexamplecom"""

text = """
Subject: Sat54, Nov 1981for cab75le
Date: tMon, 26 Aug 2002 16:26:01 -Truk1700
DeliverTuert15o: July2024 z@localhost2440.example.com Thu26 June2023
"""

# text = """
# Sat54Nov1981
# Mon26Aug2002
# Thu26June2023
# """

# text ="""
# SubjectPla5478nsforcable
# DateMon26Aug2002162601Truk1700
# Delivered-Tozzz22z@localhostexamplecom"""

# text ="Subject: Pla5478ns for cable Date: Mon, 26 Aug 2002 16:26:01 -Truk1700 Delivered-To: zzz*22 z@localhost.example.com"


# text = "Date: Mon, 26 Aug 2002 16:26:01 -1700"
# text = """
# Subject: Pla5478ns for cab75le
# Date: tMon, 26 Aug 2002 16:26:01 -Truk1700
# DeliverTue15o: July2024 z@localhost2440.example.com"""


def find_dates_in_text_1(text):
    dw = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    mnt = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
           'December']

    lst = []
    pcl = r"[^a-zA-Z0-9]"
    pt = r"[A-Z]\w{2}[a-zA-z]?\d{2,4}"

    cl_tx = re.sub(pcl, "", text)

    res = re.findall(pt, cl_tx)

    return res


# print(list(find_dates_in_text_1(text)))


def find_dates_in_text_2(text):
    dw = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    mnt = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
           'December']

    lst = []
    pcl = r"[^a-zA-Z0-9]"
    pt = r"([A-Z]\w{2}[a-zA-z]?\d{2}[A-Z]\w{2}[a-zA-z]?\d{4})"
    # gpt = r"[A-Z][a-zA-Z]{2}\d{2}[A-Z][a-zA-Z]{2,3}\d{2}(?:\d{2})?"
    cl_tx = re.sub(pcl, "", text)
    res = re.findall(pt, cl_tx)

    return res


# print(list(find_dates_in_text_2(text)))


def find_dates_in_text_3(text):
    dw = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # mnt = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    mnt = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07',
           'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}

    day_week = {'Mon': '01',
                'Tue': '02',
                'Wed': '03',
                'Thu': '04',
                'Fri': '05',
                'Sat': '06',
                'Sun': '07'}

    lst = []
    pcl = r"[^a-zA-Z0-9]"
    pt = r"([A-Z]\w{2}[a-zA-z]?\d{2}[A-Z]\w{2}[a-zA-z]?\d{4})"
    # gpt = r"[A-Z][a-zA-Z]{2}\d{2}[A-Z][a-zA-Z]{2,3}\d{2}(?:\d{2})?"
    p_num = r"([a-zA-Z]+)"
    comp = re.compile(r"([a-zA-Z]+)")
    cl_tx = re.sub(pcl, "", text)
    res = re.findall(pt, cl_tx)
    for i in res:
        data = re.findall(p_num, i)
        print(day_week[data[0]], data[1])
    return res


# print(list(find_dates_in_text_3(text)))




def find_dates_in_text_4(text):
    dw = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # mnt = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    mnt = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07',
           'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}

    # day_week = {'Mon': '01',
    #             'Tue': '02',
    #             'Wed': '03',
    #             'Thu': '04',
    #             'Fri': '05',
    #             'Sat': '06',
    #             'Sun': '07'}

    lst = []
    pcl = r"[^a-zA-Z0-9]"
    # p_date для отбора вхождений date
    p_date = r"\d{2}[A-Z][a-zA-Z]{2,4}\d{2}(?:\d{2})?"
    # p_word_fethc шаблон для групп
    p_word_fethc = r"(\d+)([a-zA-Z]+)(\d+)"
    comp = re.compile(p_word_fethc)
    # cl_tx очищенная единая строка
    cl_tx = re.sub(pcl, "", text)
    res = re.findall(p_date, cl_tx)

    for date in res:
        print(date)
        matched = comp.match(date)
        lst.append(matched.group(2))
        # month_select = [[i for j in mnt.keys() if i in j] for i in matched.group(2)]
        month_select = [[i for j in mnt.keys() if i in j] for i in lst]
        print(month_select)
        yield matched.group(2)


# print(list(find_dates_in_text_4(text)))



def find_dates_in_text_7(text):
    dw = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # mnt = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    mnt = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07',
           'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}

    # day_week = {'Mon': '01',
    #             'Tue': '02',
    #             'Wed': '03',
    #             'Thu': '04',
    #             'Fri': '05',
    #             'Sat': '06',
    #             'Sun': '07'}

    lst = []
    pcl = r"[^a-zA-Z0-9]"
    # p_date для отбора вхождений date
    p_date = r"\d{2}[A-Z][a-zA-Z]{2,4}\d{2}(?:\d{2})?"
    # p_word_fethc шаблон для групп
    p_word_fethc = r"(\d+)([a-zA-Z]+)(\d+)"
    comp = re.compile(p_word_fethc)
    # cl_tx очищенная единая строка
    cl_tx = re.sub(pcl, "", text)
    res = re.findall(p_date, cl_tx)

    for date in res:
        print(date)
        matched = comp.match(date)
        month = matched.group(2)
        yield matched.group(2)


# print(list(find_dates_in_text_7(text)))

def find_dates_in_text_5(text):

    month = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07',
           'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}

    # day_week = {'Mon': '01',
    #             'Tue': '02',
    #             'Wed': '03',
    #             'Thu': '04',
    #             'Fri': '05',
    #             'Sat': '06',
    #             'Sun': '07'}

    lst = []
    pattern_clean = r"[^a-zA-Z0-9]"
    # p_date для отбора вхождений date
    pattern_date = r"\d{2}[A-Z][a-zA-Z]{2,4}\d{2}(?:\d{2})?"
    # p_word_fethc шаблон для групп
    p_word_fethc = r"(\d+)([a-zA-Z]+)(\d+)"
    compil_date = re.compile(p_word_fethc)
    # cl_tx очищенная единая строка, в text всё меняем на "" кроме a-zAZ0-9
    clean_text = re.sub(pattern_clean, "", text)
    # в очищенной строке cl_tx ищем совпадения по шаблону p_date
    match_res = re.findall(pattern_date, clean_text)

    for date in match_res:
        # компилируем шаблон из compil_date с вхождениями date из res
        matched = compil_date.match(date)
        month_prefix = matched.group(2)
        # конвертация названия месяца в номер месяца
        for key, value in month.items():
            if month_prefix in key:
                yield matched.group(3), value, matched.group(1)



print(list(find_dates_in_text_5(text)))