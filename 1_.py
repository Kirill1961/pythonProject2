a = [0.98, 0.14, 0.44, 0.13, 0.09, 0.19, 0.53, 0.7]


def ou(x):

    def ine(y):
        return x * y

    return ine(5)


print(ou(2), "ok")

g = (["q", "w", "e", "r"], ["q", "w", "e", "r"], ["q", "w", "e", "r"])

with open("names.csv", "r") as n:
    while True:
        n_ = n.readline()
        print(n_)
        if not n_:
            break

k = 10
print(f"{k}")

p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 12, 13, 4, 56, 78, 12, 32, 65, 98, 87, 54, 55]
print(len(p))

months_31 = "january,  march,  may,  july, august,  october, december"
months_30 = "april, june, september, november"
month_28_29 = "february"
# month = input("enter month :")
# print(month)
# if months_31.find(month) >= 0:
#     print(month, "31 days")
# elif months_30.find(month) >= 0:
#     print(month, "30 days")
# else:
#     print("February 28 or 29 days")

def count_vs_while(x):
  if x < 1000:
    print(x)
    return True
  return False
x = 2
while count_vs_while(x):
  x *= 10
count_vs_while(2)


def caesar_cipher(text):
    result = ""
    for char in text:
        if char.isalpha():                        # буква ли это
            shift_char = ord(char) + 3
            if char.isupper():                    # большая ли это буква
                result += chr(shift_char) if shift_char <= ord("Z") else chr(shift_char - 26)
            else:
                result += chr(shift_char) if shift_char <= ord("z") else chr(shift_char - 26)
        else:
            result += char
    return result

text = input("Введите фразу: ")
encrypted_text = caesar_cipher(text)
print("Зашифрованный текст: ", encrypted_text)