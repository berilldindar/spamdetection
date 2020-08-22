# This is code to separate Train Emails and Test Emails.
import os
from shutil import copyfile
import random
import nltk

abc = ['ham','spam']
for x in abc:
    for y in range(6):
        path = r"C:\Users\beril\OneDrive\Masaüstü\Proje2\enron"+str(y+1)+"/"+x+"/"
        percent_70 = (0.7)*len(os.listdir(path))
        a = []
        for j in range(len(os.listdir(path))):
            a.append(j)
        b = random.sample(a, int(percent_70))
        for i in b:
            copyfile(path+"/"+os.listdir(path)[i], r"C:\Users\beril\OneDrive\Masaüstü\Proje2\kopyalananlar"+os.listdir(path)[i])
        for v in range(len(os.listdir(path))):
            c = os.listdir(path)[v]
            train_path = r"C:\Users\beril\OneDrive\Masaüstü\Proje2\kopyalananlar"
            h = os.listdir(train_path)
            if c not in h:
                copyfile(path+"/"+c, r"C:\Users\beril\OneDrive\Masaüstü\Proje2\kopyalananlar2"+c)