# Imports
import requests
from bs4 import BeautifulSoup
import re
import tkinter
from tkinter import *
from tkinter.constants import PIESLICE
import time




# Root win build
root = tkinter.Tk()
root.title('Odpytywacz drukarek v0.1')
root.geometry('700x500')

text_box = tkinter.Text(root, width = 100, height = 300)
text_box.grid(row = 50, column = 0, columnspan = 2)

# IP list read
lista = []
with open('ip.txt', 'r') as plik:
    for line in plik:
        lista.append("http://"+line[:-1])

time.sleep(3)


# Main app and loop
lista2 = []

for ip in lista:
    url = ip
    headers = {
    'User-Agent': 'Mozilla/5.0',
    'From': 'youremail@domain.com'}
    try:
        reqs = requests.get(url, headers = headers, timeout =10 ,verify=False)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        row = soup.find('h2')
        row1 = soup.find('h3')
        s1 = str(row)
        result = re.search('>(.*)<', s1)
        s2 = str(row1)
        result1 = re.search('color="(.*)/font>', s2)
        result2 = re.search('>(.*)<', str(result1))

        lista2.append(str(url) + " ][ " + str(result.group(1)) + " ][ " + str(result2.group(1)) + "\n")
    except requests.exceptions.Timeout:
         lista2.append(str(ip) + " ][ " + "Drukarka nie odpowiada" + " ][ " + "Drukarka nie odpowiada" + "\n")

text_box.insert(tkinter.INSERT, lista2)



root.mainloop()
