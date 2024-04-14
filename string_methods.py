#!/usr/bin/env python

sentence ='what is good for the goose is good for the gander '
print(sentence)

count=0

for i in sentence:
    if i=="a":
        count= count +1

print('The count of a in sentence is ' + str(count))

modified_sentence = sentence.replace('a','z')
print(modified_sentence)

