# -*- coding: utf-8 -*-
"""Wordle latest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GOeoWURrKEDqP98p_H9uWMTM9ktVNaie
"""

import random
import os
from colorama import Fore
import nltk
os.system('cls')
nltk.download('words')
words = nltk.corpus.words.words()
all_words=[]    #Also contains the five letter words with repeating characters
word_list=[]    #Only contains valid five letter words and target word is picked from this list
os.system('cls')
print("Welcome to Wordle!")
prompt=r'''      _.--._  _.--._
,-=.-":;:;:;\':;:;:;"-._
\\\:;:;:;:;:;\:;:;:;:;:;\
 \\\:;:;:;:;:;\:;:;:;:;:;\
  \\\:;:;:;:;:;\:;:;:;:;:;\
   \\\:;:;:;:;:;\:;::;:;:;:\
    \\\;:;::;:;:;\:;:;:;::;:\
     \\\;;:;:_:--:\:_:--:_;:;\
      \\\_.-"      :      "-._\
       \`_..--""--.;.--""--.._=>
        "'''
print(prompt)
for word in words:
    if len(word)==5 and len(set(word))==5:
        word_list.append(word.upper())
    if len(word)==5:
        all_words.append(word.upper())
def func(word_list):
    count=0
    l_list=[]
    target=random.choice(word_list)
    #print(target)
    sum=''
    hints=''
    a=True
    while a:
        sum=''
        hints='' #hints
        while count<=6 and sum!=target: # Changed count<6 to count<=6

            user_input=input(f'Guess {count+1}: ').upper()
            sum2='' #user_input will be stripped of spaces and stored in this variable
            for i in user_input: #striping spaces from user input
                if i!=' ':
                    sum2+=i
            user_input = sum2
            if user_input not in word_list or len(user_input)!=5:
                print('Not a valid word!')
                count-=1
            else:
                for i in range(5): # Added a for loop to compare each letter
                    if user_input[i]==target[i]:
                        hints+= Fore.GREEN + user_input[i] + Fore.RESET
                    elif user_input[i] not in target:
                        hints+= Fore.RED + user_input[i] + Fore.RESET
                    else:
                        hints+=Fore.YELLOW + user_input[i] + Fore.RESET

            count+=1
            print(hints)
            hints=''
            store=sum
            sum=''

            if count==6 or store.upper()==target.upper():
                #print('break')
                a=False
                break

    print('Target word is:',target)

x='y'
loop=True
while loop:
    if x=='y':

        func(word_list)
        x=input('again? y/n :')
        os.system('cls')
    else:
        input('press enter to exit')
        loop=False