#!/usr/bin/python
import os
word_counter = 0
line_counter = 0
word = 'bitcoin'
import pdb;pdb.set_trace()
dir_to_cp_files = os.getcwd()+'/'+'bhavesh_file_dir'
url = 'https://dumps.wikimedia.org/other/pagecounts-raw/2016/2016-01/'
os.system('mkdir {}'.format(dir_to_cp_files))
os.system('wget -r -np -R "index.html*" {} -P {} '.format(url,dir_to_cp_files))
rm_header = (url.split("https://")[1]).split('/')
file_path = ''
for i in rm_header:
    file_path=file_path+i+'/'
file_path=dir_to_cp_files+'/'+file_path.replace("//","/")
for filename in os.listdir(file_path):
        if filename.endswith(".gz"):
                filename=file_path+filename
                os.system('gunzip {}'.format(filename))
                fname = filename.split(".gz")[0]
                with open(fname, 'r') as f:
                    for line in f:
                        words = line.split()
                        for i in words:
                                if word in i:
                                        word_counter=word_counter+1
print("Occurrences of the word:{}".format(word_counter))
