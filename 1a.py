import os
import sys
import glob


# path = r"D:\downloads\Spam_Asassians\spam\*"
# sys.path.append(os.path.abspath(os.path.join(path)))
# print(sys.path[-1])
# print("spam")


def l_f():
   path = r"D:\downloads\Spam_Asassians\spam\*"
   path_filse = glob.iglob(path)
   files = list(path_filse)
   print(files)
   with open(files) as file:
      word = file.read()
      word_frame = word.strip("'',").split(" ")
      print(word_frame)
l_f()