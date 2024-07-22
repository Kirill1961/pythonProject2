import os, sys
import glob  # iglob - итерирует папку
import pprint
import re


def long_word(path):
    path_files = glob.iglob(path)
    files = list(path_files)[1]
    # print(files)
    with open(files) as file:
        word = file.read()
        word_frame = word.split(" ")
        word_frame_filter = filter(lambda x: x != "", word_frame)
        # print(list(word_frame_filter))
        long_word = max(word_frame_filter, key=len)
        print(f" max len word : {len(long_word)}")
        print(f" long word : {long_word}")


long_word(r"D:\downloads\SPAM Assassian\spam\*")


# def t_p(fr, fw):
#
#     with open(inpfr, "r", encoding="cp1251") as fr:
#         rows = fr.readlines()
#         rows_fr = [
#             f"{enum} : " + row for enum, row in enumerate(rows, start=1)  # добавка к строке нумерации при чтении
#         ]
#         print(rows_fr)
#         with open(inpfw, "w", encoding="cp1251") as fw:
#             [fw.write(f" № {row.strip()}") for row in rows_fr]  # добавка к строке нумерации при записи
#         with open(inpfw, "r", encoding="cp1251") as wr:
#             write = wr.readlines()
#             print(write)
#
# fr = input(f"enter name file for read 13 : ")
# fw = input(f"enter name file for write 23 : ")
# inpfr = glob.glob(rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{fr}.txt")[0]
# inpfw = glob.glob(rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{fw}.txt")[0]
#
# t_p(fr, fw)


def add_files(*args, **kwargs):
    file_for_add = [v for k, v in kwargs.items()][0]
    print(f"file for write : {file_for_add}")
    # args уже является кортежем, дополнительная распаковка не нужна
    for name_file in args:
        file_read = glob.glob(
            rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{name_file}"
        )[0]

        file_write = glob.glob(
            rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{file_for_add}"
        )[0]

        # неправильное имя или расширение файла
        try:
            with open(file_read, encoding="utf-8") as fr:
                content = fr.read()

                # файл без контента - ошибка
                if not content:
                    print(print(f"have not content {name_file}"))
                with open(file_write, "a", encoding="utf-8") as fw:
                    fw.write(content)

        except Exception as err:
            print(f"{err};   file name '{name_file}'", "\n")


add_files("13.txt", "23.txt", " ", "14.txt", "xls_x.xlsx", add="24.txt")


# Удаление закомментированных строк
def del_coment(file_del, *, file_write):  # * - разделяет позиционные и именованные аргументы

    file_read = glob.glob(
        rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{file_del}"
    )[0]

    file_write = glob.glob(
        rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{file_write}"
    )[0]

    with open(file_read) as fd:
        file_strip = [i.strip("\n") for i in fd.readlines()]
        pprint.pp(file_strip, indent=4)
        file_split = [file.split("#")[0] for file in file_strip if file.split("#")[0]]
        pprint.pp(file_split)
        with open(file_write, "w") as fw:
            writer = fw.writelines(file_split)
        with open(file_write, "r") as fr:
            print(fr.read(), "\n")


del_coment("##.txt", file_write="2#.txt")


def regex(file_read):
    reg = re.compile("Subject(.*)X-MIME", re.MULTILINE | re.DOTALL)
    input_file = glob.glob(rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{file_read}.txt")[0]
    with open(input_file) as ifl:
        print(reg.findall(ifl.read()))
        # print(ifl.read())
regex(input("file 13, 14, 15, 70, 71, 77 : "))



