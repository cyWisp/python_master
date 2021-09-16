#!/usr/bin/env python
import sys, os
sys.path.append("./scripts")
from classes.words import Data, Mangle
from process.generate import generate_password

DATA_PATH = os.path.abspath("./data/words.json")
CHARS_PATH = os.path.abspath("./data/legend.json")

if __name__ == '__main__':
    data = Data(DATA_PATH)
    m_object = Mangle(CHARS_PATH)
    word, new_password = generate_password(data, m_object)
    print(f"{word} | {new_password}")
    
    


    