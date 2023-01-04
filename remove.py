#coding:utf-8
import os

def remove_duplicate_rows(oldtxt_path, newtxt_path): 
    # oldtxt = "./train/labels/_MG_3004_02_jpg.txt"
    # newtxt = "./train/labels2/_MG_3004_02_jpg.txt"

    outfile=open(newtxt_path, "w")

    f = open(oldtxt_path, "r")
    
    lines_seen = set()  # Build an unordered collection of unique elements.
    
    for line in f:
        line = line.strip('\n')
        if line not in lines_seen:
            outfile.write(line+ '\n')
            lines_seen.add(line)

# old_dir = './train/labels/'
# new_dir = './train/labels_new/'

# old_dir = './test/labels/'
# new_dir = './test/labels_new/'

old_dir = './valid/labels/'
new_dir = './valid/labels_new/'

#获取该目录下所有文件，存入列表中
fileList = os.listdir(old_dir)
for file in fileList:
    print(file)
    old_txt_path = old_dir + file
    new_txt_path = new_dir + file
    remove_duplicate_rows(old_txt_path, new_txt_path)