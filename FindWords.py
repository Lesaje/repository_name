import random

def word_searching (j, FIELD_SIZE):
    word_num = random.randint(100, 900)
    word = open('words.txt').read().split('\n')[word_num]
    word = list(word)                                               #making a list from our string
    word_len = len(word)
    if (word_len>(FIELD_SIZE-j)):                                     #check if we can place word in row
        word = word_searching (j, FIELD_SIZE)                         #try to find another word if we couldn't print it
    return word

FIELD_SIZE = 5                                     #NxN game field size

i=0
j=0

word_number = 0

alphabet=list(map(chr, range(97,123)))                                 

random.seed(version=2) 

word_list = list()

f = open('words.txt', 'r')

print ("Rules:")
print ("_______________________")
print ("")
print ("The console displays a plate of 30x30 characters.")
print ("")
print ("Your task is to find as many words as possible.")
print ("")
print ("Words are formed only horizontally.")
print ("")
print ("If you enter a word that is not there, you will be notified.")
print ("")
print ("When you want to end the game, enter @")
print ("_______________________")
print ("")


while (i<FIELD_SIZE):
    while (j<FIELD_SIZE):
        rand = random.randint(1, 10)                                 # in 1 of 10 cases we will print word
        if (rand==1 and FIELD_SIZE-j>2):                             # check if j not to big for placing word                                 
            word = word_searching(j, FIELD_SIZE)
            word_list.append(''.join(word))
            word_number += 1
            for k in word:
                print (k, sep = '', end = ' ')
                j += 1
        else:
            rd = random.randint(0, 25)
            print (alphabet[rd], sep = '', end = ' ')
            j += 1
    print ("") 
    i += 1
    j = 0
print ("_______________________")
print ("")
enter = input()
while (enter != '@'):
    if (enter in word_list):
        print ("Yes, this word in list")
        word_list.remove(enter)
    else:
        print("No, this word not in the list")
    enter = input()
print ("")
if (len(word_list) != 0):
    print ("You aren't find all words in the list, try other time")
    print("")
    for words in word_list:
        print (words)
        print("")
else:
    print("Great! You find all words!")