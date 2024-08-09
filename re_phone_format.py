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
        # проверяем номер на совпадение с шаблоном check_num, берём шаблон из check_num и применяем к trim_phone
        matched = check_num.match(trim_phone)
        # проверяем размер номера, долж == 11
        if len(trim_phone) == 11 and matched:
            print("\t" * 4, f"Убираем символы -> {check_un_symb}")
            num_st.append(f"+7({matched[1]})-{matched[2]}-{matched[3]}")
        else:
            num_st.append("invalid")
    return f" result = {num_st}"

print(validate_and_format_phones(phones))


