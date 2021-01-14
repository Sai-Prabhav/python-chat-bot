import re
import speech_recognition as sr
import json
from lib import *
from lib2 import *
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
funcdict = {
    "find lowest common multiple": math_functions.LowestCommonMultiple,
    "roll a dice": roll_a_dice,
    "open file": open_file,
    "subtract number": sub,
    "toss a coin": toss,
    "add numbers": add,
    "search": search,
    "give me some dumy text": dumy,
    "dumy": dumy,
    "help": helpx,
    "find square": square,
    "find square root": squareroot,
    "time": date_time.time,
    "date": date_time.date,
    "encrypt": cryptography.encrypt,
    "decrypt": cryptography.decrypt,
    "find common factors": math_functions.commonfactors,
    "find factors": math_functions.factors,
    "isprime": math_functions.isPrime,
    "find highest common factor": math_functions.highestCommonFactor,
    "find multiples": math_functions.multiples,
    "find nearest perfect square": math_functions.NearestPerfectSquare,
    "is perfect square": math_functions.IsPerfectSquare,
    "find lowest Form": math_functions.lowestForm,
    "riddle": riddle
}
great = ["Thankyou", "So nice of you", "I appreciate for your help", "thank you very much",
         "I thank you from the bottom of my heart. Yes, I do have it", "accept my endless gratitude", "thanks a lot"]

print("Hi, I'm your friend you can ask me questions but not sure I can answer all ")
print("If you are enough having fun with me say 'stop'  ")
print("loading database")
tdata = load_database()
mainlist = [funcdict, data]
while True:
    s = tell('say somthing')
    i = re.sub("\s\s+", " ", s)
    if i == "stop" or i == "s":
        break
    if i == '':
        print("you didnt enter anything")
        continue
    status = False
    if i == "test 123":
        for key, values in funcdict.items():
            print(key)
            values()
    for data in mainlist:
        if mainlist.index(data) == 0:
            if data.get(i):
                data.get(i)()
                status = True
        elif data.get(i):
            print(data.get(i))
            status = True
    if status == False:
        if tdata.get(i):
            print("one of your friend or you said the answer is :")
            print(tdata.get(i))
            b = tell("is it true?? type yes or no ").lower()
            if b == "yes":
                data[i] = tdata[i]
            elif b == "no":
                string = tell("what is the correct answer?:")
                tdata[i] = string
            else:
                print(
                    'sorry i dont understand but next time make sure you you only type "yes" or "no" ')
            print(choice(great)+" for your answer")
        else:
            print(
                "I dont know the answer can you help me!!, you can tell me the answer or say sorry")
            a = tell("help me with answer :")
            if a != "sorry":
                print(choice(great))
                tdata[i] = a
            else:
                print("its ok")
review = tell("how was your experience?:")
path = find_database_path()
with open(path, "r") as jsonFile:
    data = json.load(jsonFile)
data["user_review"].append(review)
with open(path, "w") as jsonFile:
    json.dump(data, jsonFile, indent=4)
print("saving database")
save_database(tdata)
print(choice(great))
