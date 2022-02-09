import os
import time
import threading
import random

wordlist = "about|above|add|after|again|air|all|almost|along|also|always|America|an|and|animal|another|answer|any|are|around|as|ask|at|away|back|be|because|been|before|began|begin|being|below|between|big|book|both|boy|but|by|call|came|can|car|carry|change|children|city|close|come|could|country|cut|day|did|different|do|does|don't|down|each|earth|eat|end|enough|even|every|example|eye|face|family|far|father|feet|few|find|first|follow|food|for|form|found|four|from|get|girl|give|go|good|got|great|group|grow|had|hand|hard|has|have|he|head|hear|help|her|here|high|him|his|home|house|how|idea|if|important|in|Indian|into|is|it|its|it's|just|keep|kind|know|land|large|last|later|learn|leave|left|let|letter|life|light|like|line|list|little|live|long|look|made|make|man|many|may|me|mean|men|might|mile|miss|more|most|mother|mountain|move|much|must|my|name|near|need|never|new|next|night|no|not|now|number|of|off|often|oil|old|on|once|one|only|open|or|other|our|out|over|own|page|paper|part|people|picture|place|plant|play|point|put|question|quick|quickly|quite|read|really|right|river|run|said|same|saw|say|school|sea|second|see|seem|sentence|set|she|should|show|side|small|so|some|something|sometimes|song|soon|sound|spell|start|state|still|stop|story|study|such|take|talk|tell|than|that|the|their|them|then|there|these|they|thing|think|this|those|thought|three|through|time|to|together|too|took|tree|try|turn|two|under|until|up|us|use|very|walk|want|was|watch|water|way|we|well|went|were|what|when|where|which|while|white|who|why|will|with|without|word|work|world|would|write|year|you|young|your".split("|")
WORDS_PER_LINE = 7
TIME = 60 
ended = False

count = 0
errors = 0

clear = lambda: os.system('clear')

def delay(delay):
    time.sleep(delay)
    
def counter():
    pass

def countdown(amount):
    time.sleep(amount)
    global ended
    ended = True
    
def check_countdown():
    global ended
    global errors
    while True:
        if ended:
            clear()
            print("Du hast in " + str(TIME) + " Sekunden " + str(count) + " Wörter erreicht und dabei " + str(errors) + " Fehler gemacht." )
            break

def game(words):
   case_sensitive = False
   current_words = []
   if input("Case sensitive (Y/N) \n> ").lower() == "y":
       case_sensitive = True
   i = 0
   while i < WORDS_PER_LINE:
       i += 1
       current_words.append(random.choice(words))
   input("Start game with settings?\nCase sensitive: " + str(case_sensitive) + "\nAny input to start")
   countdownthread = threading.Thread(target = countdown, args = (TIME, ))
   countdownthread.start()
   global count
   global errors
   while not ended:
       clear()
       print(" ".join(current_words) + "  -  Richtige Wörter: " + str(count) + "  -  Falsche Wörter: " + str(errors))
       if case_sensitive:
           if input("> ").split(" ")[0] == current_words[0]:
               count += 1
               current_words.pop(0)
               current_words.append(random.choice(words))
           else:
               errors += 1
               current_words.pop(0)
               current_words.append(random.choice(words))
       else:
           if input("> ").lower().split(" ")[0] == current_words[0].lower():         
               count += 1
               current_words.pop(0)
               current_words.append(random.choice(words))
           else:               
               errors += 1
               current_words.pop(0)
               current_words.append(random.choice(words))
        
    
thread = threading.Thread(target = game, args = (wordlist, ))
thread.start()
thread2 = threading.Thread(target = check_countdown)
thread2.start()
