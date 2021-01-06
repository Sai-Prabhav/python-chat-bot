import requests  
from time import sleep
from random import randint,choice
from bs4 import BeautifulSoup

def search ():
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
    n1 = int(input("give me first number"))
    n2 = int(input("give me second number"))
    print(n1-n2)


def add():
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
