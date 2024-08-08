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
Subject: Pla5478ns for cab75le
Date: Mon, 26 Aug 2002 16:26:01 -Truk1700
Delivered-To: zzz122 z@localhost2440.example.com"""


# text ="""
# SubjectPla5478nsforcable
# DateMon26Aug2002162601Truk1700
# Delivered-Tozzz22z@localhostexamplecom"""

# text ="Subject: Pla5478ns for cable Date: Mon, 26 Aug 2002 16:26:01 -Truk1700 Delivered-To: zzz*22 z@localhost.example.com"


# text = "Date: Mon, 26 Aug 2002 16:26:01 -1700"
def find_dates_in_text(text):
    lst = []
    pcl = r"[^a-zA-Z0-9]"
    pt = r"\w{3}\d{2,4}"
    # for tx in text.split(" "):
    # print(tx)
    cl_tx = re.sub(pcl, "", text)
    print(cl_tx)
    # lst.append(re.findall(pt, cl_tx))
    res = re.findall(pt, cl_tx)
    print(res, "..")
    for i in res:
        print(i)
        # lst_dt = lst.append(i)
        yield i, ">>"


list(find_dates_in_text(text))