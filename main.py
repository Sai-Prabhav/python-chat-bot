import re
import sys
import os
import json
from lib import *
from random import *
from time import *

data = {"who are teachers": "I simple say god",
        "who are you": "I'm your friend you can ask me questions and i try to answer them byut may not know all of them but sure learn it with you",
        "do you have a teacher": "No, but you can be my teacher by just teaching me what I dont know",
        "who old are you": "I was born when you ran the my program",
        "do you have frinds": "Yes its you!!!!!",
        "can you eat": "No I only take data as my food",
        "why is teachers day celebrated": "The birth date of the second President of India, Sarvepalli Radhakrishnan, 5 September 1888, has been celebrated as Teacher's Day since 1962.",
        "when is teachers day celebrated": "Globally, Teachers Day is celebrated on 5th October; in India, we celebrate it on 5th September from 1962 onwards.",
        "who is the greatest teacher in india": "Your best teacher is your last mistake,” Kalam said.",
        "who started teachers day in india": "Dr Sarvepalli Radhakrishnan said 'Instead of celebrating my birthday, it would be my proud privilege if September 5 is observed as Teachers Day' he said"
        }

great = ["Thankyou", "So nice of you", "I appreciate for your help", "thank you very much",
         "I thank you from the bottom of my heart. Yes, I do have it", "accept my endless gratitude", "thanks a lot"]
help_options = [
    "Answer few of your questions.", "Roll a dice.", "Toss a coin", "Subtract number", "Add numbers" , "find factorial"
]

print("Hi, I'm your friend you can ask me questions but not sure I can answer all ")
print("If you are enough having fun with me say 'stop'  ")

def find_database_path():
    relative_path = sys.argv[0]
    letter_list = [x for x in relative_path]
    slashindex = []
    lix = ["\ "]   
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
def save_database(data):
    path = find_database_path()
    data1 = {"tdata":data}
    with open(path, "w") as jsonFile:
        json.dump(data1,jsonFile,indent=4)  
print("loading database")
tdata = load_database()
while True:
    s = input("tell me your question plz.. ").lower().strip()
    i = re.sub("\s\s+", " ", s)
    if i == "stop":
        break
    elif i == "s":
        break
    elif i == "help":
        for item in help_options :
          print(item)
     elif i == "roll a dice":
        roll_a_dice()

    elif i == "subtract number":
        t = input("do you want to add numbers say yes or no ").lower()
        if t == "yes":
            sub()
    elif i == "toss a coin":
        toss()

    elif i == "add numbers":
        t = input("do you want to add numbers say yes or no ").lower()
        if t == "yes":
            add()
    elif i == "search":
        search()
    elif i == "give me some dumy text" or i == "dumy":
        dumy()
    elif data.get(i):
        print(data.get(i))
    else:
        if tdata.get(i):
            print("one of your friend or you said the answer is :")
            print(tdata.get(i))
            b = input("is it true?? type yes or no ").lower()
            if b == "yes":
                data[i] = tdata[i]
            elif b == "no":
                string = input("what is the correct answer?:")
                tdata[i] = string
            else:
                print('sorry i dont understand but next time make sure you you only type "yes" or "no" ')
            print(choice(great)+" for your answer")
        else:
            print("I dont know the answer can you help me!!, you can tell me the answer or say sorry")
            a = input("help me with answer :")
            if a != "sorry":
                print(choice(great))
                tdata[i] = a
            else:
                print("its ok")
print("saving database")
save_database(tdata)
print(choice(great))
