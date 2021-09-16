#!/usr/bin/env python
import os, json

class Data:
    def __init__(self, path):
        self.path = path
        with open(self.path, 'r+') as data_file: 
            self.data = json.load(data_file)
    
    def get_nouns(self):
        return self.data['nouns']
    def get_adjectives(self):
        return self.data['adj']
    def get_adverbs(self):
        return self.data['adv']

class Mangle:
    def __init__(self, chars_path):
        with open(chars_path, 'r+') as chars_file: 
            self.chars = json.load(chars_file)
    
    def mangle(self, word):
        new_word = list()
        for letter in word:
            if letter.upper() not in self.chars.keys(): new_word.append(letter)
            else:
                for k, v in self.chars.items():
                    if letter == k.lower() and k is not v:
                        new_word.append(v)
                
        return "".join(new_word)

    