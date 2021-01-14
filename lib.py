import requests
from time import sleep
from random import randint, choice
from bs4 import BeautifulSoup
import sys
import os
import json
import math
import speech_recognition as sr
help_options = ["Answer few of your questions.", "Roll a dice.", "Toss a coin",
                "Subtract number", "Add numbers", "find factorial", 'riddle', 'open file']


def tell(a):
    r = sr.Recognizer()
    with sr.Microphone() as scro:
        sleep(0.5)
        print(f'bot: {a}')
        adio = r.listen(scro)
        ans = r.recognize_google(adio)
        print(f'you: {ans}')
        return ans


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
    if os.path.exists(path):
        with open(path, "r") as jsonFile:
            data = json.load(jsonFile)
        tdata = data["tdata"]
        with open(path, "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)
    else:
        initial_data = {
            "tdata": {},
            "user_review": []
        }
        with open(path, "w") as jsonFile:
            json.dump(initial_data, jsonFile, indent=4)
        with open(path, "r") as jsonFile:
            data = json.load(jsonFile)
        tdata = data["tdata"]
        with open(path, "w") as jsonFile:
            json.dump(data, jsonFile, indent=4)
    return tdata


def square():
    n = int(input("What number you want to square:"))
    if n == '':
        n = 0
    print(n*n)


def squareroot():
    x = int(input("What number you want to find square root of:"))
    if x == '':
        x = 0
    print(math.sqrt(x))


def helpx():
    for item in help_options:
        print(item)


def save_database(data):
    path = find_database_path()
    with open(path, "r") as jsonFile:
        data1 = json.load(jsonFile)
    data1["tdata"] = data
    with open(path, "w") as jsonFile:
        json.dump(data1, jsonFile, indent=4)


def search():
    name = input("what you want to search: ")
    if name == '':
        print("you didnt enter anything..")
    else:
        URL = "https://en.wikipedia.org/wiki/"+name
        heders = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.211"}
        page = requests.get(URL, heders)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.findAll("p")
        print(title[2].text)
        print(title[3].text)


def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


def roll_a_dice():
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
    n1 = int(input("give me first number: "))
    n2 = int(input("give me second number: "))
    print(n1-n2)


def add():
    n = int(input("who many numbers do you want add: "))
    y = 0
    for i in range(n):
        x = int(input('your number:'))
        y += x
    print(y)


def toss():
    print(choice(["Heads", "Tails"]))


def dumy():
    numP = int(input("who many paras you want: "))
    URL = "https://www.lipsum.com/feed/html"
    heders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.211"}
    page = requests.get(URL, heders)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.findAll("p")
    for i in range(numP):
        print(title[i].text)


def dumytext():
    numwords = int(input('num words you want:'))
    for i in range(numwords):
        numletters = randint(2, 6)
        x = ["q", "w", "e", "r", "t", "y", 'u', 'i', 'o', 'p', 'a', 's', 'd',
             'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        word = ''
        for i in range(numletters):
            cl = choice(x)
            word = word+cl
    print(word, end=' ')


def sayhi():
    hi = ["hi", "hey", "hello", "hope you are good", "how are you ", "how is your day", "hi there",
          "hello!", "I'm good!", "fine! how about you ?", "hello friend", "hope you are good too!"]
    print(randon.choice(hi))


def riddle():
    URL = "https://www.prodigygame.com/main-en/blog/riddles-for-kids/"
    heders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 OPR/72.0.3815.211"}
    page = requests.get(URL, heders)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find_all('div')
    divindex = []
    questions = []
    answers = []
    for diva in div[35:]:
        q = diva.findAll("strong")
        e = diva.findAll("p")
        for pa in q:
            pa = pa.text
            if pa[1] == '.' or pa[2] == '.':
                questions.append(pa)
        for em in e:
            em = em.text
            if em[6] == ':':
                answers.append(em)
    ran = choice(range(len(answers)))
    print(questions[ran][2:])
    print(answers[ran][7:])


def open_file():
    pathlist = {}
    print('You can save file loction so thay you can open it later or open the saved files. Say "go back" to leav')
    run = True
    while run:
        s = input(
            'What you want to do?? You can say file name of what you want to open or tell "save" to save the file location: ')
        i = re.sub("\s\s+", " ", s)
        if i == 'go back':
            run = False
        if i == 'save':
            x = input('what is the path of exe file: ')
            y = input('what is the name of the application: ')
            pathlist[y] = x
            print('saved the path')
        elif pathlist.get(i):
            os.startfile(pathlist.get(i))

        else:
            print('file not found concider adding it to path')
