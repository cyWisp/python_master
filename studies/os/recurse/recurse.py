#!/usr/bin/env python
import os, argparse

def main():
        
        parser = argparse.ArgumentParser()
        parser.add_argument('-p', type=str, default='', help='Path to list')
        args = parser.parse_args()
        
        directory = args.p
        
        print('Directory as initial input: {}\n'.format(args.p))
        
        abs_directory = os.path.abspath(directory)
        
        print('Directory converted to absolute path: {}\n\n'.format(abs_directory))
        
        sub_list = []
        sub_files = []
        
        for root,  subs, files in os.walk(directory):
                print('Root: {}\n'.format(root))
                print('sub folders: {}\n'.format(subs))
                print('files: {}\n'.format(files))
                sub_list.append(subs)
                sub_files.append(files)
                
        for sub in sub_list:
                print(sub)
                
        for f in sub_files:
                print(f)
                
                
                    
        
                
                
                

        
        
        
if __name__ == '__main__':
        main()