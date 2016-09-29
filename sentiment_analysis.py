# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 01:55:56 2016

@author: Dhruv
"""

afinnfile = open(r"C:/Users/Dhruv/Documents/GitHub/datasci_course_materials/assignment1/AFINN-111.txt","r")
scores = {} # initialize an empty dictionary
for line in afinnfile:
  term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  scores[term] = int(score)

afinnfile.close()

print(scores.items())

sentiment = 0 
sword = 0
uword = 0 

with open(r"C:\Users\Dhruv\.spyder2-py3\targaryen.txt","r") as f:
    for line in f:
        for word in line.split():
            #sword = sword + 1
            #print(word)
            try :
                print("Parsing\n") 
                sentiment = sentiment + scores[word]
                sword = sword + 1
            except KeyError:
                sentiment = sentiment + 0
                uword = uword + 1
                #print("Useless word")

adjusted_sentiment = sentiment/sword

print(adjusted_sentiment)

'''
in_file = open(r"C:/Users/Dhruv/.spyder2-py3/output.txt", "r")
out_file = open("result.csv","a")
for line in in_file:
    words = line.split()
    #print("Inside the loop \n")
    sword = sword + 1
    word = words.pop()
    print(word+"\n")

print(sword)

    try :
        print(word+"\n") 
        sentiment = sentiment + scores[word]
        sword = sword + 1
    except KeyError:
        sentiment = sentiment + 0
        uword = uword + 1
        print("Useless word")
'''