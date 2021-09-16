#!/usr/bin env python
import time, os, sys

class Chapter():
    
    def __init__(self, option):
        
        self.option = option
        self.chapter = ""
                
    def getQuiz(self):

        while True:
        
            os.system('clear')
            time.sleep(1)
            chapterMenu()
            chapterChoice = getInput()
            self.chapter = str(chapterChoice)
            
            if self.chapter == '1':
                
                #print("\n\nchoice 1 selected")
                #time.sleep(1)
                loadQuiz(self.chapter)
            
            elif self.chapter == '2':
                
                print("\n\nchoice 2 selected")
                time.sleep(1)
                
            elif self.chapter == '3':
                
                print("\n\nchoice 3 selected")
                time.sleep(1)
                
            elif self.chapter == '4':
                
                break
                
            
        mainLoop()
        
def mainLoop():
    
    while True:
        
        os.system('clear')
        time.sleep(1)
        mainMenu()
        newChapter = Chapter(getInput())
        
        if newChapter.option == '1':
            
            #print("option 1 selected")
            newChapter.getQuiz()
        
        elif newChapter.option == '2':
            
            print("\n\noption 2 selected")
            time.sleep(1)
            
        elif newChapter.option == '3':
            
            print("\n\noption 3 selected")
            time.sleep(1)
        
def load():        
    
    os.system('clear')
    time.sleep(1)
    
    loadString = "Now Loading!!!!"
    length = len(loadString)
    
    for iteration in range (0,3):
        for index, character in enumerate(loadString):
            if index == (length -1):
                print(character)
                os.system('clear')
                time.sleep(.08)
            else:
                print(character, sep='', end='', flush=True)
                time.sleep(.08)

def loadQuiz(chapter):    
        
    chapter = str(chapter.strip())
    print(chapter)
    
    numChapter = "ch_" + chapter + ".txt"
    try:
        with open(numChapter, 'r') as newFile:
            newFile.write("test")
    except:
        print("could not open file")
    finally:
        newFile.close()
    
    

def mainMenu():
        
    print("\t Quiz Ver. 2\n")
    print("1. Select Chapter")
    print("2. Start Quiz")
    print("3. Exit\n\n")

def chapterMenu():

    print("Select Chapter: \n")
    print("1. Chapter 1: intro to blah")
    print("2. Chapter 2: doing blah with blah")
    print("3. Chapter 3: more on blah")
    print("4. Back\n\n")
        
def getInput():
    
    userInput = input("$_ ")
    return str(userInput)



#=========================START OF MAIN================================
def main():

    #load()
    mainLoop()
    
if __name__=='__main__':
    main()