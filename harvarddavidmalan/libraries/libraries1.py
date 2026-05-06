"""
import random

escalacao = random.choice(["jorginho", "arrascaeta"])
print(escalacao)

#2
import random

number = random.randint(1, 10)
print(number)

#3

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


#4
import statistics

print(statistics.mean([100, 90]))

#5
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Receba o erro")
#6
import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too few arguments")   
else:
    print("hello, my name is ", sys.argv[1])   

#7
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too few arguments")

print("hello, my name is", sys.argv[1]) 

#8
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg) #take the slices here to list 

#9
import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)       

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
    cowsay.trex("hello, " + sys.argv[1])
"""
import requests
import sys

if len(sys.argv)  != 2:
    sys.exit()   

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term="  + sys.argv[1])
print(response.json())   