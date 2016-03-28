#! usr/bin/env python

f= open("hi.txt", "r")
lista={}
for line in f :
    line = line.split()
    for word in line:
        if word in lista.keys():
            lista[word]+=1
        else:
            lista[word]=1
for key in lista.keys():
    print key,"-->", str(lista[key])


