import random
import string

print('hello, Welcome to my Password Generator. Made with love')

length = int(input('Enter the length of password: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all,length)

password = "".join(temp)

print(password)