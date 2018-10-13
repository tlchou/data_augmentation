import os


DATA_DIR = './result/cut_after_rotate'
f = open("list.txt", 'w+')

for filename in os.listdir(DATA_DIR):
    length = len(filename)
    list_name = filename[0:length-4]
    f.write(list_name+'\n')