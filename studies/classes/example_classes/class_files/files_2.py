#!/usr/bin/env python
import time, os, sys, string

class FileMaker():
    
    def __init__(self):
        
        self.fileName = ""
        
    def setFileName(self, fName):
        
        fName = input("File Name: ")
        self.fileName = str(fName + ".txt")
    
    def createFile(self):
        
        tempName = self.fileName
        tempName.strip()
        
        try:
            with open(tempName, 'w') as newFile:
                tempText = input("text: ")
                newFile.write(str(tempText))
        except:
            print("could not open file")
        finally:
            print("File has been written...")

def main():
    
    nfm = FileMaker()
    file_name = ''
    
    nfm.setFileName(file_name)
    nfm.createFile()
    
    
    
if __name__ == '__main__':
    main()