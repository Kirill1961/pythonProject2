import os
import sys
import glob


# path = r"D:\downloads\Spam_Asassians\spam\*"
# sys.path.append(os.path.abspath(os.path.join(path)))
# print(sys.path[-1])
# print("spam")


def l_f():
   # path = r"C:\Users\Kirill\Desktop\spamAsassian\spam\0161.00e60d1a3478f1ae99ff49fbd4b30605"
   path = r"C:\Users\Kirill\Desktop\spamAsassian\spam\*"
   path_filse = glob.iglob(path)
   files = list(path_filse)
   len_files = len(files)
   n = -1
   while n <= len_files:
      n += 1
      with open(files[n]) as file:
         word = file.read()
         word_frame = word.strip("'',").split(" ")
         print(word_frame)
l_f()