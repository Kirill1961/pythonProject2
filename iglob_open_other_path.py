import os, sys
import glob  # iglob - итерирует папку
import pprint


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


def t_p():
    ...
    # fr = input(f"enter name file for read 13 : ")
    # fw = input(f"enter name file for write 23 : ")
    #
    # inpfr = glob.glob(rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{fr}.txt")[0]
    # inpfw = glob.glob(rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{fw}.txt")[0]
    # with open(inpfr, "r", encoding="cp1251") as fr:
    #     rows = fr.readlines()
    #     rows_fr = [
    #         f"{enum} : " + row for enum, row in enumerate(rows, start=1)  # добавка к строке нумерации при чтении
    #     ]
    #     print(rows_fr)
    #     with open(inpfw, "w", encoding="cp1251") as fw:
    #         [fw.write(f" № {row.strip()}") for row in rows_fr]  # добавка к строке нумерации при записи
    #     with open(inpfw, "r", encoding="cp1251") as wr:
    #         write = wr.readlines()
    #         print(write)


t_p()


def add_files(*args, **kwargs):
    file_for_add = [v for k, v in kwargs.items()][0]
    # print(file_for_add)
    for (
        name_file
    ) in args:  # args уже является кортежем, дополнительная распаковка не нужна
        file_read = glob.glob(rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{name_file}")[
            0
        ]
        file_write = glob.glob(
            rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{file_for_add}"
        )[0]

        with open(file_read) as fr:
            try:
                file_for_add = fr.read()
                print(file_for_add)
                with open(file_write, "a") as fw:
                    fw.write(file_for_add)
            except Exception as err:
                print(f"UnicodeDecodeError: {err};   file name '{name_file}' ")
                # file_for_add = fr.read()
                # with open(file_write, "w") as fw:
                #     fw.write(file_for_add)

            # file_write = glob.glob(rf"C:\Users\Kirill\Desktop\spamAsassian\ASS\{*args}.txt")[0]


add_files("13.txt", "do_c.doc", "14.txt", add="24.txt")
