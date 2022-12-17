import secrets
import string
import random

special = "!#$*%?@&"

x = 16

special_nbr = 1
while special_nbr <= 1:
    special_nbr = secrets.randbelow(int(x/4))
special_rand = ""
for _ in range(special_nbr):
    special_rand += special_rand.join(special[secrets.randbelow(8)])

nbr_nbr = 1
while nbr_nbr <= 1:
    nbr_nbr = secrets.randbelow(int(x/2))
nbr_rand = ""
for _ in range(nbr_nbr):
    nbr_rand += nbr_rand.join(string.digits[secrets.randbelow(10)])

password = special_rand + nbr_rand
remaining_len = x - nbr_nbr - special_nbr

for _ in range(remaining_len):
    password += password.join(string.ascii_letters[secrets.randbelow(52)])

temp = list(password)
random.shuffle(temp)
final_password = "".join(temp)
print(final_password)
