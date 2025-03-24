import os
from random import randint

for i in range(0, 100):
    x = randint(15, 35)
    for j in range(x):
        d = str(i) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d+'\n')
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push -u origin main')