import random
import string
# from tkinter.tix import Tree
# letters = string.ascii_lowercase
# print ( ''.join(random.choice(letters)))
# def fane_name(s):
n_time = int(input("Enter number name:"))
for i in range(n_time):
    name_funy = input('Name:')
    while True:
        letters = string.ascii_lowercase
        # letters2 = random.choice(letters)
        # name_fane + letters2
        p=(name_funy+(random.choice(letters)))
        print(p)
        break
            
    