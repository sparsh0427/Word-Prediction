import re
from nltk.util import ngrams
import random

list_original = [
"I love the world and the things in it",
" I love the way cheetah runs",
" I am a man of honor",
" I will be a rich guy",
" I am a teenager so I am a rebel",
" I am an iconoclast and a fighter",
" I believe in education",
" I love everything",
" I watch a movie every day",
" I hate pollution",
" I love the work of god",
" I love the beauty of this world",
" I adore the way people try solve hard things",
" I am nothing but a blade of grass",
" I will unleash a lot of prophecies and will bring down hordes of legions unto this earth to destroy you",
" I love doing things in a peculiar way",
" I love and hate probability It is so stupid and fun at the same time",
" I love the way software programs work",
" I love my room"
]

string_original = "".join(list_original) 

list_each_word = string_original.split(" ")
count_each_word = len(list_each_word)

#unique ONE word

unique_words_one = set(list_each_word)

#Combing 1 words 
i = 2
list_split_one =list((ngrams(list_each_word, i)))
count_list_one = len(list_split_one)






#unique TWO word

list_unique_two = []
combine = ""
for i in range(0,count_each_word - 2):
    combine = list_each_word[i] + " " + list_each_word[i+1]
    list_unique_two.append(combine)

unique_words_two = set(list_unique_two)    

#Combing 2 words 

list_two = []
combine_two = ""

for i in range(0,count_each_word - 2):
    combine_two = list_each_word[i] + " " + list_each_word[i+1]
    list_two.append(tuple((combine_two,list_each_word[i+2])))

count_list_two = len(list_two)

    
    
    
    
#unique THREE word


list_unique_three = []
combine = ""
for i in range(0,count_each_word - 3):
    combine = list_each_word[i] + " " + list_each_word[i+1] + " " + list_each_word[i+2]
    list_unique_three.append(combine)

unique_words_three = set(list_unique_three)

#Combing 3 words 

list_three = []
combine_three = ""

for i in range(0,count_each_word - 3):
    combine_three = list_each_word[i] + " " + list_each_word[i+1] + " " + list_each_word[i+2]
    list_three.append(tuple((combine_three,list_each_word[i+3])))
    
count_list_three = len(list_three)
    
    

    
    
#unique FOUR word

list_unique_four = []
combine = ""
for i in range(0,count_each_word - 4):
    combine = list_each_word[i] + " " + list_each_word[i+1] + " " + list_each_word[i+2] + " " + list_each_word[i+3]
    list_unique_four.append(combine)

unique_words_four = set(list_unique_four)

#Combing 4 words 

list_four = []
combine_four = ""

for i in range(0,count_each_word - 3):
    combine_four = list_each_word[i] + " " + list_each_word[i+1] + " " + list_each_word[i+2]
    list_four.append(tuple((combine_four,list_each_word[i+3])))
    
count_list_four = len(list_four)

#All possible words for 1 words
dict_one_words = {}

for i in unique_words_one:
    l = []
    for j in range(0,count_list_one):
        if(i == list_split_one[j][0] and i != list_split_one[j][1]):
            l.append(list_split_one[j][1])
    dict_one_words[i] = l
    
    
#All possible words for 2 words
dict_two_words = {}

for i in unique_words_two:
    l = []
    for j in range(0,count_list_two):
        if(i == list_two[j][0] and i != list_two[j][1]):
            l.append(list_two[j][1])
    dict_two_words[i] = l


#All possible words for 3 words
dict_three_words = {}

for i in unique_words_three:
    l = []
    for j in range(0,count_list_three):
        if(i == list_three[j][0] and i != list_three[j][1]):
            l.append(list_three[j][1])
    dict_three_words[i] = l
    

#All possible words for 4 words
dict_four_words = {}

for i in unique_words_four:
    l = []
    for j in range(0,count_list_four):
        if(i == list_four[j][0] and i != list_four[j][1]):
            l.append(list_four[j][1])
    dict_four_words[i] = l
    
n = int(input("Number of Words you would enter : "))
string = input("Enter the string : ")
if(n == 1):
    print()
    print("Possible words with string ",string," are :")
    print()
    print(set(dict_one_words[string]))
    print()
    print("Current prediction with string",string," is : ")
    print(random.choice(dict_one_words[string]))
elif(n == 2):
    print()
    print("Possible words with string ",string," are :")
    print()
    print(set(dict_two_words[string]))
    print()
    print("Current prediction with string",string," is : ")
    print(random.choice(dict_two_words[string]))
elif(n == 3):
    print()
    print("Possible words with string ",string," are :")
    print()
    print(set(dict_three_words[string]))
    print()
    print("Current prediction with string",string," is : ")
    print(random.choice(dict_three_words[string]))
elif(n == 4):
    print()
    print("Possible words with string ",string," are :")
    print()
    print(set(dict_four_words[string]))
    print()
    print("Current prediction with string",string," is : ")
    print(random.choice(dict_four_words[string]))

print()
n = int(input("Enter the length of random sentence : "))
string = input("Enter the starting word for the random sentence :")
combine_random = []
combine_random.append(string)
for i in range(0,n-1):
    string_temp = combine_random[-1]
    string = random.choice(dict_one_words[string_temp])
    combine_random.append(string)
print()
print("Random Sentence generated = ")
print()
print(" ".join(combine_random))
