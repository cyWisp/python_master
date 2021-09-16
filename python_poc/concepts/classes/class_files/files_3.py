#!/usr/bin/env python
import time, os, sys

class FileSuite():
    
    def __init__(self):
        
        self.loadString = "Loading...."
        self.userInput = ""
    
    def load(self):
        
        loadMessage = str(self.loadString)
        length = len(loadMessage)
        
        os.system('clear')
        time.sleep(1)

        for iteration in range(0,3):
            for index, character in enumerate(loadMessage):
                if index == (length -1):
                    print(character)
                    os.system('clear')
                    time.sleep(.08)
                else:
                    print(character, sep='', end='', flush=True)
                    time.sleep(.08)
        
    def showMenu(self):
            
        print("\tFile Practice Program 1.9.2\n\n")
        print("1. create file")
        print("2. read file")
        print("3. exit")
        
    def takeInput(self, uInput):
            
        uInput = input("$_ ")
        self.userInput = str(uInput)
            

def main():
    
    newFs = FileSuite()
    newFs.load()
    newFs.showMenu()
    
    choice = ''
    newFs.takeInput(choice)
    
    print("You inputted: {}".format(newFs.userInput))
    time.sleep(3)
    
    
    
    
if __name__=='__main__':
    main()