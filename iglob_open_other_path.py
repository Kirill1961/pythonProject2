import os, sys
import glob
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


def t_p(path):

    # i_fr = input(f1)
    # i_fw = input(f2)
    # ifr = glob.iglob(r"C:\Users\Kirill\Desktop\spamAsassian\ASS\*")
    i_fr = glob.glob(fr"C:\Users\Kirill\Desktop\spamAsassian\ASS\{path}.txt")[0]
    # print(ifr)

    with open(i_fr) as fr:
        rows = fr.readlines()
        row = map(lambda x: x.strip("\n "), rows)
        rows_fr = filter(lambda x: x != "", row)
        pprint.pprint(list(rows_fr))
t_p(13)