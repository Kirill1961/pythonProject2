from typing import List


class Solution:

    def substring(self, s: str, words: List[str]) -> List[int]:
        self.s = s
        self.words = words
        num = 0
        len_sub = len(words) * len(words[0])
        print(len(s))
        st = 0
        output = []
        self.output = output
        while num < len(s):
            num += 1
            st += 1
            len_sub += 1
            for v in [s]:
                b = list(v[st - 1:len_sub - 1])
                set_res = set()
                for headlist in [b[ind:ind + len(words[0])] for ind in range(0, len(b), len(words[0]))]:
                    set_res.add(''.join(headlist))
                # print(set(words), set_res)
                if set(words) == set_res:
                    output.append(num - 1)
        return output

    def __str__(self):
        return str(self.output)
        # print('index of initial letters    ', output)
        # return  output


ind_substring = Solution()
ind_substring.substring('barfoofoobarthefoobarman', ['bar', 'foo', 'the'])
print(ind_substring)



# ЗАготовка функции для вышенаписанного класса



s = ['barfoothefoobarman'] # 18
w = ['foo','bar']


print(set(''.join(w)))

num = 0
sub_s = ['foo','bar']
len_sub = len(sub_s) * len(sub_s[0])
len_s = sum(len(i) for i in s)
len_while = len_s - len_sub
st = 0
sp = len_sub
output = []
while num < len_while:
    num += 1
    st += 1
    sp += 1
    for v in s:
        a = set(sub_s)
        b = v[st - 1:sp - 1]
        p = {str(b[0:2]), str(b[2:4]), str(b[4:])}
        print(num, a, p)
        if a == p:
            output.append(num-1)
            print(output)
