import random

lotto_num = []
while len(lotto_num) < 7:
    lotto_number = random.randint(1,46)
    if not lotto_number in lotto_num:
        lotto_num.append(lotto_number)
print(lotto_num)