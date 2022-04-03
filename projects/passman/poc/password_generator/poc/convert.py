#!/usr/bin/env python
import os, json

if __name__ == '__main__':
    data_path = os.path.abspath("../../data/")
    files = [os.path.join(data_path, x) for x in os.listdir(data_path)]
    
    data = dict()
    for f in files:
        with open(f, 'r+') as data_file:
            data[f.split('/')[-1].replace(".txt","")] = [x.replace("\n", "") for x in data_file.readlines()]

    
    with open(f"./data.json", "w+") as write_file:
        json.dump(data, write_file)
     
    # for k, v in data.items():
    #     print(f"{k}\n")
    #     for i in v:
    #         print(i)
    #     print()