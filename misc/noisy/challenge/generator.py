from math import floor
import random

noise = ""
with open("filter.txt", "r") as filter:
    noise = filter.read().replace("\n", "")

def gen_flag(length, chars):
    result = "".join([
        chars[random.randint(0, len(chars) - 1)] for _ in range(length) 
    ]) 
    return result

chars = "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN1234567890_"
length = input("Enter flag length (default 25): ")
length = int(length if length != "" else "25")
flag =  f"ingeneer{{{gen_flag(length, chars)}}}"
print(f"flag = {flag}")

noisy_text_length = 10000
flag_char_space = floor(noisy_text_length / len(flag))
def get_next_flag_char_index(chars_included = 0):
    if (chars_included >= len(flag)):
        return -1 
    return min(max(
        0, 
        chars_included *
            flag_char_space +
            (-1 if random.randint(0, 1) else 1) * random.randint(0, (flag_char_space - 2) // 2)
    ), noisy_text_length - 1)

noisy_text = ""
next_flag_char_index = get_next_flag_char_index()

added_flag_chars = 0
result = ""
next_char_index = get_next_flag_char_index(added_flag_chars)
count = 0
for i in range(noisy_text_length):
    count += 1
    if i == next_char_index:
        result += flag[added_flag_chars % len(flag)]
        added_flag_chars += 1
        next_char_index = get_next_flag_char_index(added_flag_chars)
        continue
    result += noise[random.randint(0, len(noise) - 1)]

def normalize(text, line_length):
    result = ""
    for i in range(len(text)):
        if i % line_length == 0:
            result += "\n"
        result += text[i]
    return result

content = normalize(result, 90)
with open("file.txt", "w") as output:
    output.write(content)
