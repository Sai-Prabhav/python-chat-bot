import requests  
from time import sleep
from random import randint,choice
from bs4 import BeautifulSoup
import sys
import os
import json
import math

help_options = ["Answer few of your questions.", "Roll a dice.", "Toss a coin", "Subtract number", "Add numbers" , "find factorial"]
def find_database_path():
    relative_path = sys.argv[0]
    letter_list = [x for x in relative_path]
    slashindex = []
    lix = ["\ "]   
    if lix[0][0] not in letter_list:
        return "database.json"
    else:
        for item in letter_list:
            if item == lix[0][0]:
                indexx = letter_list.index(lix[0][0])
                slashindex.append(indexx)
                letter_list[indexx] = "a"
        return relative_path[0:slashindex[-1]]+"\database.json"

def load_database():
    path = find_database_path()
    print(path)
    if os.path.exists(path):
        with open(path, "r") as jsonFile:
            data = json.load(jsonFile)
        tdata = data["tdata"]
        with open(path, "w") as jsonFile:
            json.dump(data,jsonFile,indent=4)
    else:
        initial_data = {
            "tdata":{}
        }
        with open(path, "w") as jsonFile:
            json.dump(initial_data,jsonFile,indent=4)
        with open(path, "r") as jsonFile:
            data = json.load(jsonFile)
        tdata = data["tdata"]
        with open(path, "w") as jsonFile:
            json.dump(data,jsonFile,indent=4)
    return tdata
def square():  
    n=int(input("What number you want to square:") )
    print(n*n)

def squareroot():  
    x=int(input("What number you want to find square root of:") ) 
    print(math.sqrt(x))

def helpx():
    for item in help_options:
        print(item)
    
def save_database(data):
    path = find_database_path()
    data1 = {"tdata":data}
    with open(path, "w") as jsonFile:
        json.dump(data1,jsonFile,indent=4)

def search():
    name=input("what you want to search: ") 
    URL="https://en.wikipedia.org/wiki/"+name
    heders = { "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.211"}
    page = requests.get(URL,heders)
    soup= BeautifulSoup(page.content, 'html.parser')
    title=soup.findAll("p")
    print(title[2].text)
    print(title[3].text)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

def roll_a_dice ():
    print("your number is ", end="", flush=True)
    sleep(1)
    print(".", end="", flush=True)
    sleep(1)
    print(".", end="",  flush=True)
    sleep(1)
    print(".", end="", flush=True)
    sleep(1)
    print(randint(1, 6))

def sub():
    t = input("do you want to subtract numbers say yes or no ").lower()
    if t == "yes":
        n1 = int(input("give me first number"))
        n2 = int(input("give me second number"))
        print(n1-n2)

def add():
    t = input("do you want to add numbers say yes or no ").lower()
    if t == "yes":
        n = int(input("who many numbers do you want add "))
        y=0
        for i in range(n):
            x= int(input('your number'))
            y+=x
        print(y)

def toss():
    print(choice(["Heads", "Tails"]))

def dumy():
    numP=int(input("who many paras you want: ") )
    URL="https://www.lipsum.com/feed/html"
    heders = { "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.211"}
    page = requests.get(URL,heders)
    soup= BeautifulSoup(page.content, 'html.parser')
    title=soup.findAll("p")
    for i in range(numP):
        print (title[i].text)
def dumytext():     
    numwords=int(input('num words you want'))
    for i in range(numwords):
        numletters=randint(2,6)
        x = ["q","w","e","r","t","y",'u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
        WORD=''
        for i in range(numletters):
            cl=choice(x)
            WORD=WORD+cl
    print(WORD, end=' ')
