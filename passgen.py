import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
symbols = "()[]{},.;/*_-"

all = lower+upper+numbers+symbols

length = 16
password="".join(random.sample(all, length))
print("Your strong password is: {}".format(password))
charcounter=len(password)
print("Quantity of characters on your pass: {}".format(charcounter)) #Para contar a quantidade de letras, numbers e symbols gerados.