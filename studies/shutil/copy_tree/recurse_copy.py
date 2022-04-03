#!/usr/bin/env python
import os, shutil, argparse

def main():
        
        #doesn't work with ../
        
        parser = argparse.ArgumentParser()
        parser.add_argument('source', type=str, default='', help='Source')
        parser.add_argument('target', type=str, default='', help='Target')
        args = parser.parse_args()
        
        #source_dir = os.path.join('.', args.source)
        #target_dir = os.path.join('.', args.target)
        
        source_dir = os.path.abspath(args.source)
        target_dir = os.path.abspath(args.target)
        
        str_source = str(args.source)
        
        print('arg_1: {}\narg_2: {}'.format(source_dir, target_dir))
        
        children = []
        
        for root, dirs, files in os.walk(target_dir):
                for d in dirs:
                        children.append(d)
        for c in children:
                new_dir = os.path.join(target_dir, c)
                new_path = new_dir + '/' + str_source
                shutil.copytree(source_dir, new_path)
                
        
        
if __name__ == '__main__':
        main()