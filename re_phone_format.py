import re

phones = ["+8 909-212-9930", "+3*9202160048", "7^999999a", "7/920216/00/(48)"]


def validate_and_format_phones(phones):
    num_st = []
    for num_phone in phones:
        # Убираем все символы кроме цифр
        pat_un_symb = r"\D"
        check_un_symb = re.findall(pat_un_symb, num_phone, re.MULTILINE)

        # компилируем шаблоны для очистки и проверки совпадения
        trim = re.compile(r"\D")
        check_num = re.compile(r"(?:\+|7|8)([0-9]{3})([0-9]{3})([0-9]{4})")

        # очищаем номер от ненужных символов
        trim_phone = trim.sub("", num_phone)
        print(f" clean phone -> {trim_phone}")
        # проверяем номер на совпадение с шаблоном check_num
        matched = check_num.match(trim_phone)
        # проверяем размер номера, долж == 11
        if len(trim_phone) == 11 and matched:
            print("\t" * 4, f"Убираем символы -> {check_un_symb}")
            num_st.append(f"+7({matched[1]})-{matched[2]}-{matched[3]}")
        else:
            num_st.append("invalid")
    return f" result = {num_st}"

# print(validate_and_format_phones(phones))

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

r_word_togeth_my = r"(?:[A-Z]\w{2}[a-zA-z]?\d{2}[A-Z]\w{2}[a-zA-z]?\d{4})"

r_word_togeth_gpt = r"[A-Z][a-zA-Z]{2}\d{2}[A-Z][a-zA-Z]{2,3}\d{2}(?:\d{2})?"

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


print(list(find_dates_in_text_1(text)))


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


print(list(find_dates_in_text_2(text)))


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


print(list(find_dates_in_text_3(text)))
